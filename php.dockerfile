FROM php:8-fpm-alpine

ENV PHPGROUP=laravel
ENV PHPUSER=laravel

RUN adduser -g ${PHPGROUP} -s /bin/sh -D ${PHPUSER}

RUN sed -i "s/user = www-date/user = ${PHPUSER}/g" /usr/local/etc/php-fpm.d/www.conf
RUN sed -i "s/group = www-date/group = ${PHPGROUP}/g" /usr/local/etc/php-fpm.d/www.conf

RUN apk add --no-cache postgresql-dev \
    && docker-php-ext-install pdo pdo_pgsql \
    && apk add --no-cache python3

CMD ["sh", "-c", "php-fpm -y /usr/local/etc/php-fpm.conf && php /var/www/html/artisan migrate:fresh"]
