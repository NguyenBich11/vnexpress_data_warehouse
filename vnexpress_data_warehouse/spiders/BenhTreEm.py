
import scrapy
import csv

class BenhtreemPySpider(scrapy.Spider):
    name = "BenhTreEm.py"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/be-gai-viem-co-tim-sau-hai-tuan-sot-sieu-vi-4758207.html',
        'https://vnexpress.net/be-trai-suy-tim-nang-do-khong-dieu-tri-benh-bam-sinh-4744799.html',
        'https://vnexpress.net/can-thiep-ngay-sau-sinh-cho-be-gai-di-tat-tim-nang-4742387.html',
        'https://vnexpress.net/ca-mo-tim-be-gai-tu-ky-can-nao-bac-si-4691484.html',
        'https://vnexpress.net/me-tieu-duong-thai-ky-co-sinh-con-di-tat-4678643.html',
        'https://vnexpress.net/tam-soat-benh-tim-bam-sinh-tu-bao-thai-tang-co-hoi-song-cho-tre-4631623.html',
        'https://vnexpress.net/kham-ho-hap-phat-hien-benh-tim-bam-sinh-4615410.html',
        'https://vnexpress.net/be-hay-om-vat-chay-nhay-met-phat-hien-benh-tim-bam-sinh-4611925.html',
        'https://vnexpress.net/sieu-am-thai-co-phat-hien-benh-tim-bam-sinh-khong-4609642.html',
        'https://vnexpress.net/nguc-lom-bam-sinh-khi-nao-can-phau-thuat-4609009.html',
        'https://vnexpress.net/benh-tim-bam-sinh-co-chua-duoc-khong-4608583.html',
        'https://vnexpress.net/cuu-song-be-6-ngay-tuoi-bi-teo-hep-mach-mau-chinh-nuoi-tim-4606819.html',
        
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('BenhTreEm.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)