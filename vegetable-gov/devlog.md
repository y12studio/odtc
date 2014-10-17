
## Fri Oct 17 10:07:56 CST 2014

remove [jpetazzo/nsenter](https://github.com/jpetazzo/nsenter)

replace docker-enter to docker exec

```
$ curl -sSL https://get.docker.com/ | sudo sh
$ sudo docker version
Client version: 1.3.0
Client API version: 1.15
Go version (client): go1.3.3
Git commit (client): c78088f
OS/Arch (client): linux/amd64
Server version: 1.3.0
Server API version: 1.15
Go version (server): go1.3.3
Git commit (server): c78088f



```


## Thu Oct 16 20:22:03 CST 2014

```
{
  "_index": "veg_life_gov",
  "_type": "veg",
  "_id": "LB21-800-2014-10-14",
  "_score": 1,
  "_source": {
    "name": "小白菜",
    "name_raw": "小白菜-蚵仔白",
    "market_id": "800",
    "price": {
      "max": 37.3,
      "avg": 16.6,
      "min": 6.3,
      "mean": 13.1
    },
    "pid": "LB21",
    "ptype": "v",
    "volume": 3942,
    "ext": "蚵仔白",
    "date": "2014-10-14",
    "market": "高雄市"
  }
}
---
{
  "_index": "veg_life_gov",
  "_type": "veg",
  "_id": "SD9-800-2014-10-03",
  "_score": 1,
  "_source": {
    "name": "洋蔥",
    "name_raw": "洋蔥-進口",
    "market_id": "800",
    "price": {
      "max": 26,
      "avg": 24.3,
      "min": 23,
      "mean": 24.1
    },
    "pid": "SD9",
    "ptype": "vi",
    "volume": 2500,
    "date": "2014-10-03",
    "market": "高雄市"
  }
}
---
{
  "_index": "veg_life_gov",
  "_type": "veg",
  "_id": "FW141-105-2014-09-25",
  "_score": 1,
  "_source": {
    "name": "星辰花",
    "name_raw": "星辰花-大湖魅力",
    "market_id": "105",
    "price": {
      "max": 65,
      "avg": 65,
      "min": 65,
      "mean": 65
    },
    "pid": "FW141",
    "ptype": "l",
    "volume": 24,
    "ext": "大湖魅力",
    "date": "2014-09-25",
    "market": "台北市場"
  }
}
----
{
  "_index": "veg_life_gov",
  "_type": "veg",
  "_id": "X1-109-2014-10-14",
  "_score": 6.165857,
  "_source": {
    "name": "蘋果",
    "name_raw": "蘋果-五爪",
    "market_id": "109",
    "price": {
      "max": 100,
      "avg": 79.6,
      "min": 60,
      "mean": 79.2
    },
    "pid": "X1",
    "ptype": "t",
    "volume": 1584,
    "ext": "五爪",
    "date": "2014-10-14",
    "market": "台北一"
  }
}
----
{
  "_index": "veg_life_gov",
  "_type": "veg",
  "_id": "X69-241-2014-10-14",
  "_score": 1,
  "_source": {
    "name": "蘋果",
    "name_raw": "蘋果-富士(進口)",
    "market_id": "241",
    "price": {
      "max": 91,
      "avg": 69.6,
      "min": 48.3,
      "mean": 69.6
    },
    "pid": "X69",
    "ptype": "ti",
    "volume": 52970,
    "ext": "富士",
    "date": "2014-10-14",
    "market": "三重市"
  }
}

```
