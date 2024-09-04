
import scrapy
import csv

class BenhnguoilonPySpider(scrapy.Spider):
    name = "BenhNguoiLon.py"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/thay-van-hai-la-cho-benh-nhan-thap-tim-lau-nam-4786873.html',
        'https://vnexpress.net/nhan-giap-tien-trien-ung-thu-4785610.html',
        'https://vnexpress.net/huyet-khoi-tinh-mach-dui-do-hoi-chung-may-thurner-4785159.html',
        'https://vnexpress.net/cuong-giap-loi-mat-do-benh-basedow-4784710.html',
        'https://vnexpress.net/phu-bach-huyet-khien-chan-trai-to-gap-doi-chan-phai-4782505.html',
        'https://vnexpress.net/mo-bac-cau-mach-vanh-khi-trai-tim-van-dap-4781937.html',
        'https://vnexpress.net/nguoi-dan-ong-nang-110-kg-bien-chung-nhoi-mau-co-tim-4781306.html',
        'https://vnexpress.net/nong-mach-cuu-cu-ba-97-tuoi-nhoi-mau-co-tim-4781084.html',
        'https://vnexpress.net/mang-nhen-tinh-mach-bao-vay-u-long-nguc-4780961.html',
        'https://vnexpress.net/kham-viem-xoang-phat-hien-u-long-nguc-to-bang-qua-le-4779743.html',
        'https://vnexpress.net/bit-lo-thong-tim-cho-nguoi-mac-nhieu-benh-nen-4779161.html',
        'https://vnexpress.net/so-cuu-dung-cach-nguoi-dot-quy-nhoi-mau-co-tim-4779280.html'
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
        with open('BenhNguoiLon.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)