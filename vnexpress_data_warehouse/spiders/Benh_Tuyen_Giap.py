import scrapy
import csv

class BenhTuyenGiapSpider(scrapy.Spider):
    name = "Benh_Tuyen_Giap"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/nhan-giap-tien-trien-ung-thu-4785610.html',
        'https://vnexpress.net/cuong-giap-loi-mat-do-benh-basedow-4784710.html',
        'https://vnexpress.net/tuong-mac-benh-tam-ly-hoa-cuong-giap-4784388.html',
        'https://vnexpress.net/buou-co-to-gay-kho-tho-4783549.html',
        'https://vnexpress.net/bach-cau-giam-manh-do-tac-dung-phu-cua-thuoc-chua-cuong-giap-4759724.html',
        'https://vnexpress.net/co-phinh-to-boi-nang-giap-4741323.html',
        'https://vnexpress.net/kham-suc-khoe-dinh-ky-phat-hien-ung-thu-tuyen-giap-4726805.html',
        'https://vnexpress.net/bat-ngo-phat-hien-ung-thu-khi-kham-suc-khoe-4725670.html',
        'https://vnexpress.net/u-tuyen-giap-lanh-tinh-hoa-ung-thu-sau-10-nam-4702762.html',
        'https://vnexpress.net/phat-hien-cuong-giap-tu-dau-hieu-kho-tho-tim-dap-nhanh-4700814.html',
        'https://vnexpress.net/suy-tim-do-cuong-giap-ma-khong-biet-4690458.html',
        'https://vnexpress.net/tuong-benh-tuoi-gia-hoa-cuong-giap-bien-chung-tim-4688789.html',
        'https://vnexpress.net/dot-ngot-noi-ngong-do-suy-giap-4685997.html',
        'https://vnexpress.net/kho-tho-boi-buou-co-khong-lo-4676134.html',
        'https://vnexpress.net/cuong-giap-khien-nguoi-dan-ong-liet-hai-chan-4669409.html',
        'https://vnexpress.net/tuong-dot-quy-hoa-u-tuyen-thuong-than-4653156.html',
        'https://vnexpress.net/suy-tim-do-giam-hormone-tuyen-giap-4644868.html',
        'https://vnexpress.net/tuong-sut-can-hoa-cuong-giap-nang-4638161.html',
        'https://vnexpress.net/phat-hien-benh-tuyen-giap-khi-kham-tim-4637591.html',
        'https://vnexpress.net/suy-giap-sau-10-nam-cat-tuyen-giap-4633800.html',
        'https://vnexpress.net/khoi-u-moc-chan-xam-lan-tuyen-giap-4622278.html',
        'https://vnexpress.net/roi-loan-nhip-tim-do-quen-uong-thuoc-tri-benh-tuyen-giap-4609253.html',
        'https://vnexpress.net/cuu-co-gai-19-tuoi-khoi-suy-tim-do-cuong-giap-4608376.html',
        'https://vnexpress.net/loan-nhip-tim-khien-nguoi-benh-cuong-giap-nguy-kich-4505434.html',
        'https://vnexpress.net/mo-buou-giap-ac-tinh-cho-benh-nhan-beo-phi-4496844.html',
        'https://vnexpress.net/cuong-giap-suy-gan-nang-o-benh-nhan-tieu-duong-4467644.html',
        
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
        with open('BenhTuyenGiap.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date','location', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
