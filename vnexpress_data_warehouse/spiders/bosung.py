
import scrapy
import csv

class BoSungSpider(scrapy.Spider):
    name = "Bo_Sung"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/nguyen-nhan-dau-bung-sau-an-trai-cay-4784293.html',
        'https://vnexpress.net/suy-kiet-do-viem-loet-dai-trang-boi-nhiem-virus-4784665.html',
        'https://vnexpress.net/nhung-mon-an-uong-co-the-gay-hoi-chung-ruot-kich-thich-4784879.html',
        'https://vnexpress.net/khoi-nguy-co-ghep-gan-nho-thay-24-lit-huyet-tuong-4779669.html',
        'https://vnexpress.net/cac-trieu-chung-tieu-hoa-canh-bao-benh-4785101.html',
        'https://vnexpress.net/7-loai-tra-giup-giam-day-hoi-4785622.html',
        'https://vnexpress.net/thu-pham-gay-ung-thu-truc-trang-4756695.html',
        'https://vnexpress.net/an-chay-co-giam-nguy-co-ung-thu-duong-tieu-hoa-4757225.html',
        'https://vnexpress.net/nhung-dieu-khong-nen-lam-sau-khi-noi-soi-tieu-hoa-4623953.html',
        'https://vnexpress.net/noi-soi-dat-stent-cho-cu-ong-co-hai-khoi-u-ac-tinh-4624282.html',
        'https://vnexpress.net/noi-soi-dat-stent-cho-cu-ong-co-hai-khoi-u-ac-tinh-4624282.html',
        'https://vnexpress.net/tai-tao-thuc-quan-bang-ong-da-day-cho-nguoi-ung-thu-4628319.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': '\n'.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'location':response.css('span.location-stamp::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('BoSung.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location','url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)