# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3

WORKDIR /usr/src/app

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider vnexpress_data_warehouse/spiders/BenhTimMach.py"]

