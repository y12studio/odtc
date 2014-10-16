FROM y12docker/estw:0.0.1

ENV APP_HOME /app/odtc-veg-live

WORKDIR $APP_HOME

ADD .  $APP_HOME
RUN pip install -r $APP_HOME/requirements.txt

#
# update kibana index json
#
RUN cd /opt/kibana/app/dashboards && \
    mv -f $APP_HOME/kibana-*.json . && \
    mv -f kibana-default.json default.json

EXPOSE 8080 9200

CMD ["/sbin/my_init"]

RUN rm -rf /tmp/* /var/tmp/*
