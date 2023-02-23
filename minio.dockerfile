FROM minio/minio:RELEASE.2022-01-08T03-11-54Z.fips

ENV MINIO_ROOT_USER=laravel
ENV MINIO_ROOT_PASSWORD=laravel

EXPOSE 9000
EXPOSE 9001

ENTRYPOINT ["minio"]
CMD ["server","/data","--console-address",":9001"]