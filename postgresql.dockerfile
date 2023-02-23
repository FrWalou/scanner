FROM postgres:latest

ENV PGDATA=/var/lib/postgresql/data/pgdata

RUN mkdir -p $PGDATA && chown -R postgres:postgres $PGDATA

VOLUME $PGDATA

USER postgres

CMD ["postgres"]