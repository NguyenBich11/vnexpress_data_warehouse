import scrapy
import csv

class PhatHienSomSpider(scrapy.Spider):
    name = "Phat_Hien_Som"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/6-bien-chung-ung-thu-phoi-4683906.html',
        'https://vnexpress.net/tai-sao-phu-nu-co-nguy-co-mac-ung-thu-phoi-cao-hon-nam-gioi-4462136.html',
        'https://vnexpress.net/cach-nhan-biet-cac-truong-hop-khan-cap-ve-ung-thu-phoi-4453067.html',
        'https://vnexpress.net/9-dau-hieu-canh-bao-benh-phoi-can-som-tam-soat-4449693.html',
        'https://vnexpress.net/6-dau-hieu-canh-bao-som-benh-ung-thu-phoi-4449179.html',
        'https://vnexpress.net/phat-hien-som-benh-ho-hap-nho-noi-soi-phe-quan-ong-mem-4444676.html',
        'https://vnexpress.net/u-phoi-lanh-tinh-phat-hien-som-se-giam-nguy-co-bien-chung-4436932.html',
        'https://vnexpress.net/hen-o-tre-nho-kho-chan-doan-4391014.html',
        'https://vnexpress.net/phan-biet-trieu-chung-covid-19-va-benh-phoi-tac-nghen-man-tinh-4381646.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-noi-soi-phe-quan-ong-mem-4351887.html',
        'https://vnexpress.net/phat-hien-cham-soc-nguoi-benh-phoi-tac-nghen-man-tinh-trong-dich-covid-19-4355556.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'location': response.css('span.location-stamp::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('PhatHienSom.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location','url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
