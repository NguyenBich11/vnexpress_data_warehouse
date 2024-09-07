import scrapy
import csv
class DaiThaoDuongSpider(scrapy.Spider):
    name = "Dai_Thao_Duong"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
         'https://vnexpress.net/mac-benh-tieu-duong-type-1-hay-type-2-nang-hon-4787888.html',
         'https://vnexpress.net/bien-chung-ban-chan-tieu-duong-ma-khong-biet-4786682.html',
         'https://vnexpress.net/6-mon-chong-viem-cho-nguoi-tieu-duong-4784664.html',
         'https://vnexpress.net/phong-tranh-dai-thao-duong-cho-tre-4783833.html',
         'https://vnexpress.net/dau-hieu-canh-bao-tang-duong-huyet-vao-ban-dem-4782698.html',
         'https://vnexpress.net/dua-cai-chua-anh-huong-den-duong-huyet-the-nao-4780416.html',
         'https://vnexpress.net/cach-phong-benh-tim-mach-do-tieu-duong-4779132.html',
         'https://vnexpress.net/tai-sao-con-tre-van-mac-benh-dai-thao-duong-4778607.html',
         'https://vnexpress.net/an-thit-lon-moi-ngay-co-tang-duong-huyet-4778290.html',
         'https://vnexpress.net/7-yeu-to-loi-song-lam-tang-nguy-co-dai-thao-duong-4778159.html',
         'https://vnexpress.net/bien-chung-dai-thao-duong-type-1-4775488.html',
         'https://vnexpress.net/dau-hieu-tre-mac-benh-tieu-duong-type-1-4775097.html',
         'https://vnexpress.net/vet-thuong-nao-canh-bao-bien-chung-ban-chan-tieu-duong-4773279.html',
         'https://vnexpress.net/mat-thi-luc-bien-chung-am-tham-do-tieu-duong-4772949.html',
         'https://vnexpress.net/loi-ich-cua-ca-rot-voi-nguoi-benh-tieu-duong-4772799.html',
         'https://vnexpress.net/an-gao-lut-co-khoi-benh-dai-thao-duong-4771994.html',
         'https://vnexpress.net/veo-chan-do-bien-chung-tieu-duong-ma-khong-biet-4771860.html',
         'https://vnexpress.net/hai-phoi-trang-xoa-do-nhiem-trung-bien-chung-ban-chan-tieu-duong-4766234.html',
         'https://vnexpress.net/nguoi-tieu-duong-nen-cao-voi-rang-may-lan-mot-nam-4763220.html',
         'https://vnexpress.net/tai-sao-nguoi-tieu-duong-thuong-bi-hu-mong-tay-chan-4760998.html',
         'https://vnexpress.net/nguyen-nhan-da-nguoi-tieu-duong-lao-hoa-nhanh-4760541.html',
         'https://vnexpress.net/benh-vong-mac-tieu-duong-4759992.html',
         'https://vnexpress.net/nhiem-trung-tu-vet-xuoc-nho-nguoi-benh-tieu-duong-phai-cat-bo-chan-4756894.html',
         'https://vnexpress.net/ha-duong-huyet-do-hoi-chung-dumping-4754055.html',
         'https://vnexpress.net/vet-xuoc-nho-tro-nang-do-bien-chung-tieu-duong-4752818.html',
         'https://vnexpress.net/ha-duong-huyet-gay-dot-quy-gia-4749306.html',
         'https://vnexpress.net/bat-ngo-phat-hien-benh-dai-thao-duong-khi-kham-vo-sinh-4738306.html',
         'https://vnexpress.net/nsut-bang-thai-bi-hoai-tu-ban-chan-do-bien-chung-tieu-duong-4737469.html',
         'https://vnexpress.net/hoai-tu-ngon-chan-do-khong-tuan-thu-dieu-tri-tieu-duong-4733422.html',
         'https://vnexpress.net/mac-benh-tieu-duong-sau-5-nam-uong-thuoc-gia-truyen-4730328.html',
         'https://vnexpress.net/lo-la-chua-tieu-duong-nguoi-phu-nu-gap-bien-chung-nang-4728271.html',
         'https://vnexpress.net/tang-duong-huyet-4720398.html',
         'https://vnexpress.net/vet-thuong-nhiem-trung-sau-ngam-vao-nuoc-muoi-4706944.html',
         'https://vnexpress.net/tuong-het-tieu-duong-nguoi-phu-nu-bi-hoai-tu-chan-boi-mun-nhot-4706551.html',
         'https://vnexpress.net/mun-nhot-nhiem-trung-gay-hoai-tu-mong-4705922.html',
         'https://vnexpress.net/nhiem-trung-da-moi-biet-bi-tieu-duong-4704527.html',
         'https://vnexpress.net/khoi-ap-xe-tu-co-lan-den-nguc-nguoi-dan-ong-4699712.html',
         'https://vnexpress.net/vet-thuong-50-nam-kho-lanh-do-tieu-duong-4694776.html',
         'https://vnexpress.net/hai-me-con-bi-bien-chung-tieu-duong-hoai-tu-chan-4688224.html',
         'https://vnexpress.net/thieu-nu-15-tuoi-hon-me-bat-ngo-phat-hien-tieu-duong-4686751.html',
         'https://vnexpress.net/suyt-mat-tinh-hoan-do-bien-chung-tieu-duong-4682982.html',
         'https://vnexpress.net/viem-bao-quy-dau-do-bien-chung-tieu-duong-4670773.html',
         'https://vnexpress.net/nhiem-trung-nang-do-bo-thuoc-tieu-duong-de-bam-huyet-4668235.html',
         'https://vnexpress.net/xem-tieu-duong-nhu-cam-cum-nguoi-dan-ong-bien-chung-nang-4646698.html',
         'https://vnexpress.net/bo-thuoc-chua-tieu-duong-nguoi-phu-nu-tang-duong-huyet-4643333.html',
         'https://vnexpress.net/suyt-chet-sau-hai-thang-uong-thuoc-nam-chua-tieu-duong-4632037.html',
         'https://vnexpress.net/nguy-kich-vi-thuong-xuyen-uong-nuoc-ngot-4608783.html',
         'https://vnexpress.net/nguoi-benh-tieu-duong-suy-da-tang-do-con-trung-chich-4595219.html',
         'https://vnexpress.net/nguy-kich-do-uong-ruou-bo-thuoc-tieu-duong-4590060.html',
         'https://vnexpress.net/virus-tan-cong-vung-kin-nguoi-dai-thao-duong-gay-lo-loet-4584547.html',
         'https://vnexpress.net/buon-non-do-cac-bien-chung-cua-benh-tieu-duong-4584593.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'location': response.css('span.location-stamp::text').get(),
            'url': response.url
        }

        # Save the extracted data to a CSV file
        with open('DaiThaoDuong.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location','url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
