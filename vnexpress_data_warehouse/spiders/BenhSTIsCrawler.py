import scrapy
import csv


class BenhstiscrawlerSpider(scrapy.Spider):
    name = "BenhSTIsCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/nhung-benh-tinh-duc-co-the-lay-qua-nu-hon-4783134.html",
        "https://vnexpress.net/tai-sao-dung-bao-cao-su-van-co-the-lay-benh-tinh-duc-4786939.html",
        "https://vnexpress.net/7-lam-tuong-ve-benh-tinh-duc-4777324.html",
        "https://vnexpress.net/hpv-co-lay-khi-hon-4775535.html",
        "https://vnexpress.net/cac-benh-tinh-duc-gay-trieu-chung-giong-cum-4770334.html",
        "https://vnexpress.net/ly-do-nen-xet-nghiem-benh-tinh-duc-4743891.html"
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
        with open('Data_BenhSTIs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        


