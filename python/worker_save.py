import redis
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Connect to Redis container
redis_container = redis.Redis(host='redis', port=6379)

# Get list of urls-to-scan
urls = redis_container.lrange('urls-to-scan', 0, -1)

# Fetch title for each URL
for url in urls:
    url = url.decode()
    if urlparse(url).scheme == '':
        url = f'https://{url}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text
    print(f"Title for {url}: {title}")
