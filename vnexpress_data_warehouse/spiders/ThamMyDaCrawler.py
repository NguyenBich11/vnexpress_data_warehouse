import scrapy
import csv


class ThammydacrawlerSpider(scrapy.Spider):
    name = "ThamMyDaCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/5-cach-ngan-seo-loi-phat-trien-4788890.html",
        "https://vnexpress.net/peel-da-bao-lau-la-du-4788041.html",
        "https://vnexpress.net/rui-ro-khi-tiem-filler-sai-cach-4787655.html",
        "https://vnexpress.net/luu-y-truoc-khi-triet-long-vinh-vien-4787438.html",
        "https://vnexpress.net/nhung-vi-tri-tren-mat-co-the-tiem-filler-4786504.html",
        "https://vnexpress.net/5-cach-thu-nho-lo-chan-long-4782138.html"
        ]

    def parse(self, response):
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': '\n'.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('Data_ThamMyDa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        


