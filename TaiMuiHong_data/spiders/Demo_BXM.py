import scrapy
import csv

class DemoBxmSpider(scrapy.Spider):
    name = "Demo_BXM"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/4-benh-mui-xoang-de-nham-lan-trieu-chung-4782494.html',
                  'https://vnexpress.net/lech-vach-ngan-mui-co-tai-phat-sau-phau-thuat-4780752.html',
                  'https://vnexpress.net/mat-khuu-giac-co-the-chua-khoi-khong-4779811.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/9-cach-don-gian-giup-giam-so-mui-4774663.html',
                  'https://vnexpress.net/nhung-hieu-lam-thuong-gap-ve-viem-xoang-4767610.html',
                  'https://vnexpress.net/cuon-mui-gian-no-do-lam-dung-thuoc-nho-mui-4767601.html',
                  'https://vnexpress.net/tre-tai-phat-viem-mui-xoang-do-di-boi-4765900.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/viem-mui-xoang-di-ung-co-can-xet-nghiem-tim-nguyen-nhan-4763199.html',
                  'https://vnexpress.net/lam-dung-thuoc-nho-mui-gay-bien-chung-4756694.html',
                  'https://vnexpress.net/tuong-u-tai-hoa-phi-dai-cuon-mui-4753783.html',
                  'https://vnexpress.net/qua-phat-cuon-mui-4753159.html'
                  'https://vnexpress.net/nen-va-khong-nen-lam-gi-khi-cam-lanh-4722959.html',
                  'https://vnexpress.net/nhieu-nguoi-chay-mau-cam-do-nang-nong-4718663.html',
                  'https://vnexpress.net/nhieu-nguoi-viem-tai-mui-hong-sau-tet-4716515.html',
                  'https://vnexpress.net/viem-mui-di-ung-mua-xuan-4711777.html',
                  'https://vnexpress.net/khoi-huong-anh-huong-den-nguoi-viem-mui-xoang-the-nao-4709688.html',
                  'https://vnexpress.net/co-nen-phau-thuat-chua-phi-dai-cuon-mui-4707483.html',
                  'https://vnexpress.net/trieu-chung-viem-mui-xoang-4707387.html',
                  'https://vnexpress.net/he-qua-kho-luong-khi-nhin-hat-hoi-4705705.html',
                  'https://vnexpress.net/8-cach-giup-giam-di-ung-4697348.html',
                  'https://vnexpress.net/tai-sao-ban-chay-nuoc-mui-4697355.html',
                  'https://vnexpress.net/dau-hieu-nhan-biet-ung-thu-mui-4694235.html',
                  'https://vnexpress.net/cach-ngan-ngua-viem-mui-di-ung-4692565.html',
                  'https://vnexpress.net/viem-xoang-chay-mau-mui-nguy-hiem-khong-4692049.html',
                  'https://vnexpress.net/dau-hieu-nhan-biet-ung-thu-xoang-4691189.html',
                  'https://vnexpress.net/cach-tranh-di-ung-voi-cay-thong-noel-4690202.html',
                  'https://vnexpress.net/su-that-thu-vi-ve-mui-nguoi-4688828.html',
                  'https://vnexpress.net/nguyen-nhan-khuu-giac-cua-ban-thay-doi-4688253.html',
                  'https://vnexpress.net/cach-don-gian-phong-viem-xoang-4687834.html',
                  'https://vnexpress.net/mo-xoang-bao-lau-hoi-phuc-4683467.html',
                  'https://vnexpress.net/an-gi-khi-chay-mau-cam-4680718.html',
                  'https://vnexpress.net/dau-dau-do-viem-xoang-dieu-tri-the-nao-4680241.html',
                  'https://vnexpress.net/trieu-chung-nhiem-trung-xoang-lan-len-nao-4676904.html',
                  'https://vnexpress.net/hep-eo-hong-nguoi-dan-ong-thuong-ngat-tho-khi-ngu-4675560.html',
                  'https://vnexpress.net/tai-sao-mui-thuong-nghet-vao-buoi-sang-4674149.html',
                  'https://vnexpress.net/nam-lap-day-cac-xoang-cua-nguoi-dan-ong-4671435.html',
                  'https://vnexpress.net/polyp-mui-co-tu-khoi-khong-4670862.html',
                  'https://vnexpress.net/7-thuc-pham-tot-cho-nguoi-benh-viem-xoang-4670701.html',
                  'https://vnexpress.net/nguyen-nhan-kho-mui-4670163.html',
                  'https://vnexpress.net/5-loai-tra-giup-giam-nghet-mui-4667503.html',
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
        with open('BenhXoangMui.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)