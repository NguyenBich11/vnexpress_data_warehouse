import scrapy
import csv

class DalieucoursecrawlerSpider(scrapy.Spider):
    name = "DaLieuCourseCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/luu-y-truoc-khi-triet-long-vinh-vien-4787438.html',
        'https://vnexpress.net/5-lam-tuong-ve-mun-4786114.html',
        'https://vnexpress.net/nhung-vi-tri-tren-mat-co-the-tiem-filler-4786504.html',
        'https://vnexpress.net/5-cach-thu-nho-lo-chan-long-4782138.html',
        'https://vnexpress.net/nhung-tinh-chat-dien-di-lam-dep-pho-bien-4780597.html',
        'https://vnexpress.net/tai-sao-dung-bao-cao-su-van-co-the-lay-benh-tinh-duc-4786939.html',
        'https://vnexpress.net/duong-chat-tu-nhien-giup-giam-ran-da-4778643.html',
        'https://vnexpress.net/cach-giam-bong-tham-mat-4775184.html',
        'https://vnexpress.net/dau-hieu-nhiem-giun-san-tren-da-4784809.html'
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
        with open('DataDaLieu.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        
