
import scrapy
import csv

class TieuhoacrawlerSpider(scrapy.Spider):
    name = "TieuHoaCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/an-uong-the-nao-de-can-bang-he-vi-sinh-duong-ruot-4787861.html',
        'https://vnexpress.net/lam-dung-khang-sinh-gay-hai-duong-ruot-the-nao-4787967.html',
        'https://vnexpress.net/lam-dung-khang-sinh-gay-hai-duong-ruot-the-nao-4787967.html',
        'https://vnexpress.net/5-gia-vi-thao-moc-tot-cho-gan-4785298.html',
        'https://vnexpress.net/5-mon-an-uong-giup-ha-men-gan-tu-nhien-4783142.html',
        'https://vnexpress.net/nhung-dieu-nen-lam-de-bao-ve-gan-4783185.html',
        'https://vnexpress.net/phat-hien-u-da-day-tu-trieu-chung-dang-mieng-4786145.html',
        'https://vnexpress.net/giam-15-kg-sau-hai-thang-mo-thu-nho-da-day-4763195.html',
        'https://vnexpress.net/tai-sao-phu-nu-de-mac-ung-thu-tui-mat-4776082.html'
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
        with open('TieuHoa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)