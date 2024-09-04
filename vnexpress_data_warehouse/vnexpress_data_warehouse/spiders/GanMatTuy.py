
import scrapy
import csv

class GanMatTuySpider(scrapy.Spider):
    name = "Gan_Mat_Tuy"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/5-mon-an-uong-giup-ha-men-gan-tu-nhien-4783142.html',
        'https://vnexpress.net/nhung-dieu-nen-lam-de-bao-ve-gan-4783185.html',
        'https://vnexpress.net/4-nhom-thuc-pham-tot-cho-nguoi-viem-tuy-4782239.html',
        'https://vnexpress.net/noi-me-day-co-phai-dau-hieu-suy-giam-chuc-nang-gan-4781330.html',
        'https://vnexpress.net/noi-me-day-co-phai-dau-hieu-suy-giam-chuc-nang-gan-4781330.html',
        'https://vnexpress.net/hang-chuc-polyp-bam-nhu-thach-nhu-trong-tui-mat-4781230.html',
        'https://vnexpress.net/vitamin-nao-tot-cho-gan-4780108.html',
        'https://vnexpress.net/loi-ich-cua-dau-nanh-voi-gan-4778700.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': '\n'.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('GanMatTuy.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)