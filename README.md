# scanner
copy .env.example to your .env
app to scan urls and take screen using docker containers
maybe it's possible to have to run command for node_modules
use: docker-compose build --no-cache
docker-compose up
if you encounter error 500 when you on localhost:4242/scanned you should re run: php artisan migrate:fresh in php container
it's possible to have to also re do python background_worker.py on python container
