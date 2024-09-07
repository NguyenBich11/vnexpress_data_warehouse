
import scrapy
import csv

class PhauThuatNoiSoiSpider(scrapy.Spider):
    name = "Phau_Thuat_Noi_Soi"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/bat-ngo-phat-hien-u-thuc-quan-khi-noi-soi-da-day-4744532.html',
        'https://vnexpress.net/beo-phi-thu-pham-gay-nhieu-benh-4705379.html',
        'https://vnexpress.net/nang-ruot-doi-khien-nguoi-dan-ong-non-oi-suot-hai-nam-4701594.html',
        'https://vnexpress.net/noi-soi-tieu-hoa-phat-hien-som-dieu-tri-khoi-ung-thu-4693418.html',
        'https://vnexpress.net/noi-soi-qua-duong-mieng-cat-u-thuc-quan-4680686.html',
        'https://vnexpress.net/thung-da-day-do-vien-thuoc-nguyen-vi-4676641.html',
        'https://vnexpress.net/tuong-bat-thuong-thai-ky-hoa-viem-ruot-thua-4663347.html',
        'https://vnexpress.net/cat-polyp-dai-trang-co-nguy-hiem-khong-4630081.html',
        'https://vnexpress.net/cu-ong-81-tuoi-chien-thang-hai-benh-ung-thu-4760404.html',
        'https://vnexpress.net/thuc-pham-nen-an-truoc-khi-noi-soi-dai-trang-4616098.html',
        'https://vnexpress.net/6-ly-do-can-noi-soi-tieu-hoa-4614443.html',
        'https://vnexpress.net/noi-soi-duong-mieng-cat-khoi-u-ac-tinh-thuc-quan-4602421.html',
        'https://vnexpress.net/7-benh-tieu-hoa-co-the-phat-hien-qua-noi-soi-4546028.html',
        'https://vnexpress.net/nhung-nguoi-nen-thuc-hien-noi-soi-tieu-hoa-4496739.html',
        'https://vnexpress.net/dieu-tri-ung-thu-gan-bang-dot-song-cao-tan-4483614.html',
        'https://vnexpress.net/kich-hoat-he-mien-dich-tieu-diet-te-bao-ung-thu-gan-4483243.html',
        'https://vnexpress.net/truyen-hoa-chat-dong-mach-gan-dieu-tri-ung-thu-gan-tien-trien-4474960.html',
        'https://vnexpress.net/noi-soi-loai-bo-khoi-u-truc-trang-khong-can-phau-thuat-4473345.html',
        'https://vnexpress.net/nut-mach-chua-ung-thu-gan-khi-khong-the-phau-thuat-4455023.html',
        'https://vnexpress.net/chua-tri-ro-hau-mon-phuc-tap-tai-phat-4453897.html',
        'https://vnexpress.net/mo-noi-soi-u-co-tron-phuc-tap-bang-robot-co-hoc-4452387.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-phau-thuat-cat-ruot-thua-4445044.html',
        'https://vnexpress.net/can-chuan-bi-gi-khi-cat-dai-trang-4443101.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-phau-thuat-giam-can-4437567.html',
        'https://vnexpress.net/nhung-luu-y-truoc-khi-thuc-hien-noi-soi-tieu-hoa-4392931.html',
        'https://vnexpress.net/lan-dau-tien-viet-nam-ung-dung-robot-cam-tay-co-hoc-vao-phau-thuat-noi-soi-4392506.html',
        'https://vnexpress.net/mo-noi-soi-cho-benh-nhan-bi-thoat-vi-thanh-bung-hiem-gap-4437169.html',
        'https://vnexpress.net/tiem-xo-noi-soi-giai-phap-chua-tri-khong-phau-thuat-4376815.html',
        'https://vnexpress.net/nhung-cau-hoi-thuong-gap-ve-phau-thuat-cat-da-day-4353861.html'
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
        with open('PhauThuatNoiSoi.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)