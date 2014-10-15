FROM y12docker/estw:0.0.1

ENV APP_HOME /app/odtc-veg-live

WORKDIR $APP_HOME

ADD .  $APP_HOME
RUN pip install -r $APP_HOME/requirements.txt

EXPOSE 8080 9200

CMD ["/sbin/my_init"]

RUN rm -rf /tmp/* /var/tmp/*
