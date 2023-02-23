import os
import redis
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import psycopg2
from datetime import datetime

# Connect to Redis container
redis_container = redis.Redis(host='redis', port=6379)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Set up PostgreSQL connection
conn = psycopg2.connect(
    host="postgres",
    database="pgsql",
    user="laravel",
    password="secret",
    port=5432
)

# Create screenshots folder if it does not exist
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

while True:
    # Get list of urls-to-scan
    urls = redis_container.lrange('urls-to-scan', 0, -1)
    if not urls:
        # Wait a bit and try again if the list is not available
        time.sleep(1)
        continue
    # Fetch title and take screenshot for each URL
    for url in urls:
        url = url.decode()
        if urlparse(url).scheme == '':
            url = f'https://{url}'

        # Set up browser and navigate to URL
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Fetch page title
        title = driver.title
        print(f"Title for {url}: {title}")

        # Take screenshot
        screenshot_filename = os.path.join('screenshots', f"{urlparse(url).netloc}.png")
        driver.save_screenshot(screenshot_filename)

        # Store data in PostgreSQL
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO websites (title, url, screen_path, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)",
                    (title, url, screenshot_filename, datetime.now(), datetime.now())
                )
                conn.commit()
                print(f"Recorded data for {url}")
        except psycopg2.Error as e:
            # Handle the exception here
            print(f"PostgreSQL error: {e}")
            conn.rollback()

        url_without_prefix = url[8:]
        print(f"Title for {url_without_prefix}")
        try:
            redis_container.lrem('urls-to-scan', 0, url_without_prefix)
            redis_container.lrem('urls-to-scan', 0, url)
        except redis.exceptions.RedisError as e:
            # Handle the exception here
            print(f"Redis error: {e}")

        # Close browser
        driver.quit()

# Close PostgreSQL connection
conn.close()