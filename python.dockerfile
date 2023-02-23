FROM python:3.9

WORKDIR /python

COPY . /python

COPY /python/requirements.txt .

RUN apt-get update && \
    apt-get install -y \
        chromium \
        libgtk-3-0 \
        libnotify-dev \
        libgconf-2-4 \
        libnss3 \
        libxss1 \
        libasound2 \
        xvfb

RUN pip install -r requirements.txt

CMD ["python", "background_worker.py"]
