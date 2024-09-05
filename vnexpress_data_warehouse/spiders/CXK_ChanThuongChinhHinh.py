import scrapy
import csv


class CxkChanthuongchinhhinhSpider(scrapy.Spider):
    name = "CXK_ChanThuongChinhHinh"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/cu-ba-4-lan-thay-khop-hang-4784727.html',
                  'https://vnexpress.net/khau-vet-rach-gan-co-vai-nguoi-dan-ong-4782050.html',
                  'https://vnexpress.net/4-yeu-to-tang-do-ben-khop-nhan-tao-sau-phau-thuat-4780443.html',
                  'https://vnexpress.net/ca-phau-thuat-gian-nan-thay-khop-cho-benh-nhan-mau-hiem-4777231.html',
                  'https://vnexpress.net/day-chang-nhan-tao-giup-nguoi-benh-di-lai-sau-chan-thuong-4774692.html',
                  'https://vnexpress.net/dau-co-chan-bat-ngo-phat-hien-u-xuong-4773295.html',
                  'https://vnexpress.net/phuc-hoi-dang-di-sau-50-nam-gay-xuong-dui-4772173.html',
                  'https://vnexpress.net/di-tat-thua-dinh-ngon-tay-o-tre-4770324.html',
                  'https://vnexpress.net/dieu-tri-chan-chu-x-nhu-the-nao-4769571.html',
                  'https://vnexpress.net/lam-the-nao-nhanh-phuc-hoi-sau-mo-thay-khop-hang-4767763.html',
                  'https://vnexpress.net/thay-khop-goi-cho-nguoi-phu-nu-beo-phi-4766466.html',
                  'https://vnexpress.net/mac-benh-truyen-nhiem-co-thay-khop-duoc-khong-4765970.html',
                  'https://vnexpress.net/cu-ba-bien-chung-thuyen-tac-phoi-sau-thay-khop-hang-4765674.html',
                  'https://vnexpress.net/nguyen-nhan-tai-dut-day-chang-sau-mo-4765139.html',
                  'https://vnexpress.net/bi-lat-co-chan-thuong-xuyen-co-nguy-hiem-4763822.html',
                  'https://vnexpress.net/5-di-tat-co-xuong-khop-bam-sinh-o-tre-nho-4762874.html',
                  'https://vnexpress.net/manh-xuong-vo-ket-trong-khop-sau-cu-nga-xe-dap-4762265.html',
                  'https://vnexpress.net/chuyen-vat-da-va-vet-loet-lo-xuong-4760697.html',
                  'https://vnexpress.net/hai-chan-cong-veo-nang-do-khop-goi-thoai-hoa-4760111.html#vn_source=Folder-SucKhoe_CacBenh_BenhCoXuongKhop_ChanThuongChinhHinh&vn_campaign=Stream&vn_medium=Item-19&vn_term=Desktop&vn_thumb=1&vn_aid=1005274',
                  'https://vnexpress.net/dut-day-chang-dau-goi-khi-nao-can-mo-4759275.html',
                  'https://vnexpress.net/ung-thu-than-di-can-xuong-sau-10-thang-khong-dieu-tri-4757882.html',
                  'https://vnexpress.net/thay-hai-khop-goi-sau-15-nam-thoai-hoa-4756823.html',
                  'https://vnexpress.net/ba-lan-dut-day-chang-gay-teo-co-long-khop-goi-4755094.html',
                  'https://vnexpress.net/cac-phuong-phap-chua-chan-vong-kieng-4753132.html',
                  'https://vnexpress.net/rach-gan-vai-benh-thuong-gap-o-nguoi-cao-tuoi-4752362.html',
                  'https://vnexpress.net/dau-co-chan-khi-chay-bo-4751932.html',
                  'https://vnexpress.net/dut-ba-day-chang-khop-goi-sau-cu-nga-xe-4751420.html',
                  'https://vnexpress.net/suyt-mat-ngon-tay-do-ket-vao-xe-day-hanh-ly-4750362.html',
                  'https://vnexpress.net/thay-ca-hai-khop-goi-do-thoai-hoa-giai-doan-cuoi-4746224.html',
                  'https://vnexpress.net/cach-giam-dau-sau-tai-tao-day-chang-4745891.html',
                  'https://vnexpress.net/thay-khop-hang-co-tap-gym-duoc-khong-4744883.html',
                  'https://vnexpress.net/thay-khop-bang-su-cho-nguoi-hoai-tu-chom-xuong-dui-4744524.html',
                  'https://vnexpress.net/gay-xuong-don-khi-choi-bong-da-4743476.html',
                  'https://vnexpress.net/thay-khop-hang-giai-phap-thay-the-chom-xuong-dui-hoai-tu-4742603.html',
                  'https://vnexpress.net/thay-hai-khop-goi-trong-mot-thang-do-thoai-hoa-nang-4741007.html',
                  'https://vnexpress.net/nghien-ruou-pha-huy-chom-xuong-dui-cua-nam-thanh-nien-4739409.html',
                  'https://vnexpress.net/di-lai-binh-thuong-sau-40-nam-khap-khieng-nho-thay-khop-hang-4738543.html',
                  'https://vnexpress.net/nhieu-nguoi-tre-phai-thay-khop-hang-4736469.html',
                  'https://vnexpress.net/tri-hoan-dieu-tri-nam-thanh-nien-dut-lien-tiep-hai-day-chang-4735281.html',
                  'https://vnexpress.net/bi-thoai-hoa-goi-co-nen-thay-khop-nhan-tao-4734933.html',
                  'https://vnexpress.net/dau-ba-vai-canh-bao-nhieu-benh-4734455.html',
                  'https://vnexpress.net/bien-dang-xuong-sau-10-nam-thoai-hoa-khop-hang-4733618.html',
                  'https://vnexpress.net/bi-dien-giat-nga-gay-nat-khop-vai-4732182.html',
                  'https://vnexpress.net/ca-si-quang-tu-bi-hoai-tu-chom-xuong-dui-4731274.html',
                  'https://vnexpress.net/ba-lan-dut-day-chang-do-choi-the-thao-4730979.html',
                  'https://vnexpress.net/tai-sao-van-dau-nhuc-sau-thay-khop-goi-4730562.html',
                  'https://vnexpress.net/rach-lon-gan-vai-gay-teo-co-4730117.html',
                  'https://vnexpress.net/thu-pham-gay-dau-bap-chan-4729099.html',
                  'https://vnexpress.net/noi-xuong-dui-cho-hai-cu-ba-u90-4727676.html',
                  'https://vnexpress.net/tai-sao-phai-tiem-chat-nhon-sau-phau-thuat-day-chang-4726668.html',
                  'https://vnexpress.net/hoai-tu-chom-xuong-dui-hai-lan-thay-khop-hang-4726307.html',
                  'https://vnexpress.net/di-lai-binh-thuong-sau-6-nam-thoai-hoa-khop-goi-4724450.html',
                  'https://vnexpress.net/ly-do-phu-nu-mac-benh-xuong-khop-cao-hon-nam-gioi-4723810.html']

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
        with open('CXK_ChanThuongChinhHinh.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
