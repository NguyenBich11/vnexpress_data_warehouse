
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
        'https://vnexpress.net/loi-ich-cua-dau-nanh-voi-gan-4778700.html',
        'https://vnexpress.net/loi-ich-cua-dau-nanh-voi-gan-4778700.html',
        'https://vnexpress.net/bi-xo-gan-an-uong-the-nao-4778210.html',
        'https://vnexpress.net/4-phuong-phap-dieu-tri-viem-tuy-cap-4775464.html',
        'https://vnexpress.net/uong-ruou-lam-ton-thuong-gan-the-nao-4775123.html',
        'https://vnexpress.net/an-gung-co-tot-cho-gan-4774650.html',
        'https://vnexpress.net/an-gung-co-tot-cho-gan-4774650.html',
        'https://vnexpress.net/nhung-dieu-nen-lam-de-bao-ve-gan-4783185.html',
        'https://vnexpress.net/4-nhom-thuc-pham-tot-cho-nguoi-viem-tuy-4782239.html',
        'https://vnexpress.net/5-thoi-quen-xau-lam-tang-nguy-co-viem-tuy-cap-4781596.html',
        'https://vnexpress.net/khoi-nguy-co-ghep-gan-nho-thay-24-lit-huyet-tuong-4779669.html',
        'https://vnexpress.net/vitamin-nao-tot-cho-gan-4780108.html',
        'https://vnexpress.net/5-loai-rau-cu-qua-ho-tro-ha-men-gan-4780481.html',
        'https://vnexpress.net/4-nhom-thuc-pham-nguoi-men-gan-cao-nen-an-4769537.html',
        'https://vnexpress.net/uong-ca-phe-loi-hay-hai-gan-4769129.html',
        'https://vnexpress.net/yeu-to-nguy-co-lam-tang-kich-thuoc-soi-tui-mat-4763637.html',
        'https://vnexpress.net/5-bo-phan-sung-tay-bat-thuong-canh-bao-benh-gan-4763456.html',
        'https://vnexpress.net/an-uong-gi-giai-doc-gan-tu-nhien-4760588.html',
        'https://vnexpress.net/thieu-ngu-lam-ton-thuong-gan-4759637.html',
        'https://vnexpress.net/benh-nao-gan-4759539.html',
        'https://vnexpress.net/4-loai-sua-tot-cho-nguoi-benh-gan-nhiem-mo-4758745.html',
        'https://vnexpress.net/nguoi-benh-xo-gan-an-thit-bo-duoc-khong-4756838.html',
        'https://vnexpress.net/lam-the-nao-ha-men-gan-4756824.html',
        'https://vnexpress.net/8-thoi-quen-giup-phong-benh-gan-4756421.html',
        'https://vnexpress.net/9-cach-giup-giam-nguy-co-mac-benh-tui-mat-4755656.html',
        'https://vnexpress.net/an-man-hai-suc-khoe-the-nao-4755900.html',
        'https://vnexpress.net/thu-pham-gay-tang-men-gan-4754439.html',
        'https://vnexpress.net/soi-tuy-co-nguy-hiem-khong-4754882.html',
        'https://vnexpress.net/nhiem-trung-duong-mat-do-soi-bit-kin-ong-gan-4755260.html',
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