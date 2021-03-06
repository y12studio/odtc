#!/bin/bash
# ------------------------------------------------------------------
# build/run/test script
# Ground Control to Major Tom
# install [docker >= 1.3](https://github.com/docker/docker)
# ------------------------------------------------------------------

set -e

IMG=y12docker/odtc-veg-live:test
GC2MT_HOME=/app/odtc-veg-live
SUBJECT=veg-live-dev
VERSION=0.1.0
USAGE="Usage: gc2mt.sh -vhxbrstc args"
DOCKER='sudo docker'
DKEXEC='sudo docker exec'
SEC_WAIT_BOOT=5

# --- Option processing --------------------------------------------
if [ $# == 0 ] ; then
    echo "$USAGE"
    exit 1;
fi

function esimport_in_container {
  cd $GC2MT_HOME
  nosetests -v --nocapture test/test_es.py
  python veg-import.py -t
  # nosetests -v --nocapture test/test_import.py
}

function cleandocker {
  $DOCKER rm $($DOCKER ps -a -q)
  $DOCKER rmi $($DOCKER images | grep "^<none>" | awk "{print $3}")
}

function build {
  echo build a test image.
  $DOCKER build -t $IMG .
}

function esimport {
  CID=$1
  echo "[SystemTest] Container " $CID
  echo "[SystemTest] boot and wait ...."
  secs=$SEC_WAIT_BOOT
  while [ $secs -gt 0 ]; do
     echo -ne "$secs\033[0K\r"
     sleep 1
     : $((secs--))
  done
  $DKEXEC $CID bash $GC2MT_HOME/gc2mt.sh -c
}

function commitimg {
  NIMGTAG=$1
  echo "[Docker Container Commit] image name " $NIMGTAG
  set +e
  FOO=$($DOCKER ps | grep $IMG)
  if [ ! -z "$FOO" ]; then
    CID=$(echo "$FOO" | awk '{print $1}')
    echo "[Docker Container Commit] " $CID
    # Warning: '--run' is deprecated, it will be removed soon. See usage.
    # [Replace 'commit --run' with 'commit --change'](https://github.com/docker/docker/pull/5105)
    # [Add support for 'commit --change'](https://github.com/docker/docker/pull/8332)
    # $DOCKER commit  --change 'CMD ["/sbin/my_init"]' $CID $NIMGTAG
    $DOCKER commit  --run='{"CMD":["/sbin/my_init"]}' $CID $NIMGTAG
    $DOCKER inspect $NIMGTAG
  else
    echo any container with image named $IMG not fund.
  fi
  set -e
}

function run {
  local CID=$($DOCKER run -p 8080:8080 -p 9200:9200 -d $IMG)
  echo "$CID"
}

function stop {
  $DOCKER ps
  # set -e exit here
  set +e
  FOO=$($DOCKER ps | grep $IMG)
  if [ ! -z "$FOO" ]; then
    echo stop a test image.
    echo FOO=$FOO
    echo "$FOO" | awk '{print $1}' | xargs $DOCKER stop
    echo [AFTER] stop the container
    $DOCKER ps
  else
    echo any image named $IMG not fund.
  fi
  set -e
}

while getopts ":vhxbrstcu:" optname; do
  case "$optname" in
    "v")
      echo "Version $VERSION"
      exit 0;
      ;;
    "x")
      echo "clean all stopped containers and all untagged images"
      cleandocker
      exit 0;
      ;;
    "b")
      build
      exit 0;
      ;;
    "r")
      run
      exit 0;
      ;;
    "t")
      stop
      build
      CID=$(run)
      $DOCKER ps
      esimport $CID
      exit 0;
      ;;
    "s")
      stop
      exit 0;
      ;;
    "u")
      commitimg "$OPTARG"
      exit 0;
      ;;
    "c")
      esimport_in_container
      exit 0;
      ;;
    "h")
      echo "$USAGE"
      exit 0;
      ;;
    "?")
      echo "Unknown option $OPTARG"
      exit 0;
      ;;
    ":")
      echo "No argument value for option $OPTARG"
      exit 0;
      ;;
    *)
      echo "Unknown error while processing options"
      exit 0;
      ;;
  esac
done

shift "$($OPTIND - 1)"

# -----------------------------------------------------------------

LOCK_FILE=/tmp/${SUBJECT}.lock

if [ -f "$LOCK_FILE" ]; then
echo "Script is already running"
exit
fi

# -----------------------------------------------------------------
trap 'rm -f $LOCK_FILE' EXIT
touch $LOCK_FILE
