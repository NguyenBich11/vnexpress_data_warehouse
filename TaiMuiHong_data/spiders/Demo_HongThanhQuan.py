import scrapy
import csv

class DemoHongthanhquanSpider(scrapy.Spider):
    name = "Demo_HongThanhQuan"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/dieu-tri-roi-loan-giong-noi-tuoi-day-thi-the-nao-4781180.html',
                  'https://vnexpress.net/ve-sinh-rang-mieng-ky-sao-hoi-tho-van-co-mui-4778484.html',
                  'https://vnexpress.net/nam-noi-giong-nu-chua-nhu-the-nao-4778128.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/viem-mui-hong-thuong-xuyen-do-va-khong-tieu-bien-4777385.html',
                  'https://vnexpress.net/tho-khi-dung-tai-nha-duoc-khong-4775466.html',
                  'https://vnexpress.net/vet-loet-do-nhiet-mieng-co-khac-ung-thu-luoi-4775220.html',
                  'https://vnexpress.net/cac-mon-nen-an-va-tranh-khi-nhiet-mieng-4774741.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/nhung-benh-thuong-gay-dau-hong-4771957.html',
                  'https://vnexpress.net/hoi-chung-ngung-tho-khi-ngu-4770417.html',
                  'https://vnexpress.net/co-nen-dung-nuoc-muoi-sinh-ly-suc-hong-rua-mui-moi-ngay-4768947.html',
                  'https://vnexpress.net/co-can-cat-thang-luoi-cho-tre-4768561.html'
                  'https://vnexpress.net/manh-xuong-ca-dam-vao-luoi-nguoi-dan-ong-4766366.html',
                  'https://vnexpress.net/meo-phong-dau-hong-ngay-nang-4765450.html',
                  'https://vnexpress.net/nguoi-lon-tuoi-co-phau-thuat-amidan-duoc-khong-4763918.html',
                  'https://vnexpress.net/ngu-ngay-co-phai-la-benh-4763644.html',
                  'https://vnexpress.net/cat-amidan-bao-lau-co-the-an-uong-binh-thuong-4761724.html',
                  'https://vnexpress.net/hoc-di-vat-mui-hong-tai-nan-thuong-gap-o-tre-nho-4760859.html',
                  'https://vnexpress.net/viem-amidan-benh-de-tai-phat-mua-he-4758338.html',
                  'https://vnexpress.net/suc-khoe/cac-benh/benh-tai-mui-hong/hong-thanh-quan-p4',
                  'https://vnexpress.net/mat-giong-do-polyp-day-thanh-quan-4751454.html',
                  'https://vnexpress.net/hoi-chung-bong-rat-mieng-4727520.html',
                  'https://vnexpress.net/5-o-chua-nhieu-mam-benh-cam-lanh-4723569.html',
                  'https://vnexpress.net/viem-amidan-hoc-mu-4719193.html',
                  'https://vnexpress.net/9-mon-an-uong-tot-cho-nguoi-dau-hong-4718648.html',
                  'https://vnexpress.net/mau-sac-o-luoi-canh-bao-benh-gi-4718257.html',
                  'https://vnexpress.net/9-benh-ve-luoi-4715719.html',
                  'https://vnexpress.net/cat-amidan-bao-lau-co-the-uong-ruou-bia-4709682.html',
                  'https://vnexpress.net/cach-nao-phong-nhiet-mieng-ngay-tet-4710048.html',
                  'https://vnexpress.net/cach-giam-kho-rat-hong-sau-khi-uong-ruou-bia-4709946.html',
                  'https://vnexpress.net/nguyen-nhan-gay-benh-luoi-trang-4708565.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-co-thanh-ung-thu-4706609.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-duoi-ham-4705269.html',
                  'https://vnexpress.net/dau-hieu-o-luoi-canh-bao-co-the-thieu-vitamin-d-4704352.html',
                  'https://vnexpress.net/tai-sao-ngay-to-hon-sau-khi-uong-ruou-4704398.html',
                  'https://vnexpress.net/meo-giam-kho-mieng-4702038.html',
                  'https://vnexpress.net/tai-sao-chay-nuoc-dai-khi-ngu-4700805.html',
                  'https://vnexpress.net/tai-sao-chay-nuoc-dai-khi-ngu-4700805.html',
                  'https://vnexpress.net/khan-tieng-canh-bao-benh-gi-4700518.html',
                  'https://vnexpress.net/sai-lam-khi-dung-nuoc-suc-mieng-4699734.html',
                  'https://vnexpress.net/nguyen-nhan-hoi-tho-co-mui-khong-do-thuc-pham-4699028.html',
                  'https://vnexpress.net/9-nguyen-nhan-gay-ngu-ngay-4698222.html',
                  'https://vnexpress.net/tai-tao-khi-quan-cho-nguoi-bi-bien-chung-sau-dot-quy-4696683.html',
                  'https://vnexpress.net/ho-khien-co-the-dot-chay-bao-nhieu-nang-luong-4695941.html',
                  'https://vnexpress.net/6-cach-lam-diu-co-hong-sau-khi-non-4694508.html',
                  'https://vnexpress.net/6-mon-an-uong-lam-tang-dom-4694925.html',
                  'https://vnexpress.net/6-mon-an-uong-tieu-dom-4693471.html',
                  'https://vnexpress.net/7-cach-loai-bo-dom-o-hong-4692983.html',
                  'https://vnexpress.net/6-mon-an-tang-mien-dich-phong-cam-cum-4689193.html',
                  'https://vnexpress.net/cach-giam-dau-hong-co-dom-mua-lanh-4687824.html',
                  'https://vnexpress.net/cam-giac-on-lanh-do-dau-4687552.html',
                  'https://vnexpress.net/phau-thuat-3-trong-1-chua-ngu-ngay-4684271.html',
                  'https://vnexpress.net/meo-bao-ve-giong-noi-trong-treo-4683942.html',
                  'https://vnexpress.net/mo-tuyen-giap-lac-cho-khien-nguoi-phu-nu-kho-nuot-4683315.html',
                  'https://vnexpress.net/tai-sao-kho-mieng-4680250.html',
                  'https://vnexpress.net/kieng-gi-khi-viem-hong-de-nhanh-khoi-benh-4678212.html',
                  'https://vnexpress.net/nguyen-nhan-gay-chua-mieng-4675373.html',
                  'https://vnexpress.net/cong-dung-giam-ho-cua-tinh-dau-4672944.html',
                  'https://vnexpress.net/viem-amidan-man-tinh-co-gay-ung-thu-4671019.html',
                  'https://vnexpress.net/ngu-ngay-nhu-sam-bat-ngo-phat-hien-viem-amidan-4668372.html',
                  'https://vnexpress.net/6-cach-giam-ngua-hong-4650860.html',
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
        with open('BenhHongThanhQuan.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)