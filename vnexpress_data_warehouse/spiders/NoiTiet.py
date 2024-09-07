import scrapy
import csv
class NoitietSpider(scrapy.Spider):
    name = "Noi_Tiet"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/ba-phuong-phap-dieu-tri-suy-tuyen-yen-4787721.html',
        'https://vnexpress.net/nhan-giap-xam-lan-sun-khi-quan-nguoi-dan-ong-4787623.html',
        'https://vnexpress.net/dau-hieu-tre-thieu-hormone-tang-truong-4782224.html',
        'https://vnexpress.net/dung-uong-sua-bo-co-ngan-day-thi-som-4777030.html',
        'https://vnexpress.net/mo-tham-my-nhan-tuyen-giap-4776624.html',
        'https://vnexpress.net/ha-canxi-mau-4771495.html',
        'https://vnexpress.net/tiem-hormone-kim-ham-day-thi-som-cho-be-gai-7-tuoi-4765899.html',
        'https://vnexpress.net/dai-thao-nhat-trung-uong-4764597.html',
        'https://vnexpress.net/suy-tuyen-thuong-than-la-benh-gi-4764233.html',
        'https://vnexpress.net/dai-thao-nhat-do-than-4752030.html',
        'https://vnexpress.net/tuong-benh-duong-ruot-hoa-suy-giap-4750597.html',
        'https://vnexpress.net/ha-kali-mau-4749619.html',
        'https://vnexpress.net/7-mon-an-bo-sung-noi-tiet-to-nu-4749226.html',
        'https://vnexpress.net/tang-huyet-ap-keo-dai-moi-phat-hien-do-u-tuyen-thuong-than-4747608.html',
        'https://vnexpress.net/tu-choi-mo-u-tuy-thuong-than-nguoi-phu-nu-nhieu-lan-tang-huyet-ap-4745304.html',
        'https://vnexpress.net/10-tu-the-yoga-giup-can-bang-noi-tiet-to-4743714.html',
        'https://vnexpress.net/loi-ich-cua-yoga-trong-dieu-hoa-noi-tiet-to-4743530.html',
        'https://vnexpress.net/meo-can-bang-noi-tiet-to-nu-4739829.html',
        'https://vnexpress.net/thieu-nu-17-tuoi-thieu-hut-90-hormone-noi-tiet-do-u-tuyen-yen-4739593.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-hoi-chung-cushing-4738977.html',
        'https://vnexpress.net/4-cach-giup-giam-can-o-tuoi-day-thi-4737260.html',
        'https://vnexpress.net/dai-thao-nhat-o-tre-em-co-nguy-hiem-4733833.html',
        'https://vnexpress.net/6-do-uong-giup-phai-dep-tang-cuong-noi-tiet-to-4731613.html',
        'https://vnexpress.net/8-meo-tang-noi-tiet-to-cho-nam-gioi-4724086.html',
        'https://vnexpress.net/lam-dung-thuoc-corticoid-giam-dau-khien-suy-tuyen-thuong-than-4712412.html',
        'https://vnexpress.net/suy-tuyen-thuong-than-dieu-tri-tai-nha-can-luu-y-gi-4693957.html',
        'https://vnexpress.net/moi-nguy-do-lam-dung-thuoc-giam-dau-chua-corticoid-4680631.html',
        'https://vnexpress.net/thua-canxi-trong-mau-co-nguy-hiem-4678388.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-tut-canxi-4677473.html',
        'https://vnexpress.net/tuong-phat-tuong-sau-ket-hon-hoa-u-tuyen-thuong-than-4675301.html',
        'https://vnexpress.net/sot-xuat-huyet-chong-benh-suy-tuyen-yen-4673655.html',
        'https://vnexpress.net/het-dau-dau-sau-mo-u-thuong-than-4670147.html',
        'https://vnexpress.net/bien-chung-sau-ba-thang-uong-thuc-pham-chuc-nang-chua-corticoid-4667402.html',
        'https://vnexpress.net/tai-sao-tre-mac-hoi-chung-cushing-4663890.html',
        'https://vnexpress.net/estrogen-tac-dong-the-nao-voi-sinh-ly-phai-dep-4660709.html',
        'https://vnexpress.net/15-thuc-pham-bo-sung-noi-tiet-to-cho-phu-nu-4655321.html',
        'https://vnexpress.net/dot-quy-tuyen-yen-la-benh-gi-4648556.html',
        'https://vnexpress.net/dai-thao-nhat-la-benh-gi-4639084.html',
        'https://vnexpress.net/an-nhieu-duong-tinh-bot-co-anh-huong-sinh-ly-nam-4636974.html',
        'https://vnexpress.net/16-dau-hieu-can-bo-sung-noi-tiet-to-nu-4636172.html',
        'https://vnexpress.net/5-cach-bao-ve-da-khoi-mun-noi-tiet-4629030.html',
        'https://vnexpress.net/9-cach-can-bang-noi-tiet-to-sau-sinh-4626722.html',
        'https://vnexpress.net/roi-loan-noi-tiet-sau-sinh-co-bat-thuong-4625512.html',
        'https://vnexpress.net/dau-hieu-nao-canh-bao-suy-giam-noi-tiet-to-4624592.html',
        'https://vnexpress.net/7-xet-nghiem-noi-tiet-to-nu-thuong-gap-4623694.html',
        'https://vnexpress.net/8-ly-do-gay-suy-giam-noi-tiet-to-nu-4614428.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-benh-tuyen-giap-4613003.html',
        'https://vnexpress.net/10-cach-can-bang-noi-tiet-to-cho-phu-nu-4610304.html',
        'https://vnexpress.net/cham-soc-da-mun-do-thay-doi-noi-tiet-the-nao-4607042.html',
        'https://vnexpress.net/lam-the-nao-nhan-biet-mat-can-bang-noi-tiet-to-nu-4606055.html',
        'https://vnexpress.net/10-benh-lien-quan-den-roi-loan-noi-tiet-4600946.html',
        'https://vnexpress.net/cach-dieu-tri-nam-da-do-thay-doi-noi-tiet-to-4596093.html',
        'https://vnexpress.net/phan-biet-nam-nang-va-nam-da-do-thay-doi-noi-tiet-4578924.html',
        'https://vnexpress.net/u-tuyen-tuy-gay-ha-duong-huyet-hon-me-4578304.html',
        'https://vnexpress.net/4-nguyen-nhan-thuong-gap-lam-thay-doi-noi-tiet-gay-nam-4574708.html',
        'https://vnexpress.net/roi-loan-noi-tiet-anh-huong-den-viem-da-co-dia-4490189.html',
        'https://vnexpress.net/hoi-chung-kallmann-gay-mat-khuu-giac-can-tro-day-thi-4487829.html',
        'https://vnexpress.net/noi-tiet-to-nu-anh-huong-the-nao-den-suc-khoe-4480771.html',
        'https://vnexpress.net/cac-benh-roi-loan-noi-tiet-thuong-gap-4479127.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-phu-nu-beo-bung-do-roi-loan-noi-tiet-4473844.html',
        'https://vnexpress.net/4-lam-tuong-ve-bo-sung-noi-tiet-to-4454353.html',
        'https://vnexpress.net/5-cach-can-bang-noi-tiet-to-de-tang-kha-nang-thu-thai-4438878.html',
        'https://vnexpress.net/nguyen-nhan-gay-roi-loan-noi-tiet-to-kho-thu-thai-4437365.html',
        'https://vnexpress.net/lieu-phap-noi-tiet-chua-khoi-ung-thu-vu-ma-khong-can-hoa-tri-3786452.html',
        
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
        with open('NoiTiet.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
