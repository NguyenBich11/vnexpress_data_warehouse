import scrapy
import csv


class BenhdalieucrawlerPySpider(scrapy.Spider):
    name = "BenhDaLieuCrawler.py"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/co-nen-dung-don-thuoc-chua-mun-trung-ca-cua-nguoi-khac-4788048.html",
        "https://vnexpress.net/5-lam-tuong-ve-mun-4786114.html",
        "https://vnexpress.net/nhieu-nguoi-nhiem-nam-viem-da-mua-mua-4785838.html",
        "https://vnexpress.net/do-mo-hoi-uot-ao-du-o-phong-dieu-hoa-la-benh-gi-4785376.html",
        "https://vnexpress.net/dau-hieu-nhiem-giun-san-tren-da-4784809.html",
        "https://vnexpress.net/cach-nao-dieu-tri-nhanh-mun-trung-ca-4784321.html"
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
        with open('Data_BenhDaLieu.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        

