FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install scrapy selenium webdriver-manager
# RUN pip install chromedriver-py
RUN pip install pymongo

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg unzip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y \
    && wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm google-chrome-stable_current_amd64.deb chromedriver_linux64.zip

COPY . .

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider vnexpress_data_warehouse/spiders/BenhTimMach.py"]
