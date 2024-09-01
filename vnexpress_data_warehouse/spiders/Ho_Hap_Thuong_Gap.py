import scrapy
import csv

class HoHapThuongGapSpider(scrapy.Spider):
    name = "Ho_Hap_Thuong_Gap"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/5-thuc-pham-giup-giam-ho-4787558.html',
        'https://vnexpress.net/che-do-dinh-duong-cho-tre-viem-duong-ho-hap-4787582.html',
        'https://vnexpress.net/4-luu-y-de-tho-dung-cach-khi-chay-bo-4787037.html',
        'https://vnexpress.net/thu-pham-gay-benh-ho-hap-o-nguoi-cao-tuoi-khi-giao-mua-4786497.html',
        'https://vnexpress.net/5-cach-ngan-mui-hoi-tho-buoi-sang-4786394.html',
        'https://vnexpress.net/phoi-ton-thuong-hinh-choi-cay-do-lao-4786367.html',
        'https://vnexpress.net/nhung-mon-an-uong-nen-tranh-khi-ho-4786135.html',
        'https://vnexpress.net/nguyen-nhan-it-ngo-gay-kho-tho-4785689.html',
        'https://vnexpress.net/7-loai-thao-moc-giup-giam-mui-hoi-tho-4785295.html',
        'https://vnexpress.net/lam-the-nao-giam-ho-nhanh-khong-dung-thuoc-4785261.html',
        'https://vnexpress.net/cam-cum-va-cam-lanh-khac-nhau-the-nao-4784903.html',
        'https://vnexpress.net/lam-the-nao-khu-mui-bia-ruou-gay-hoi-mieng-4784787.html',
        'https://vnexpress.net/duong-lay-nhiem-vi-khuan-an-thit-nguoi-4784108.html',
        'https://vnexpress.net/an-uong-the-nao-de-hoi-tho-thom-mat-4783505.html',
        'https://vnexpress.net/ly-do-phu-nu-man-kinh-thuong-ngay-ngu-4783577.html',
        'https://vnexpress.net/ban-biet-gi-ve-tho-5-ngon-tay-4783181.html',
        'https://vnexpress.net/dung-la-trau-the-nao-giam-mui-hoi-mieng-4782713.html',
        'https://vnexpress.net/lam-the-nao-phong-benh-ho-hap-cho-tre-mua-tuu-truong-4782411.html',
        'https://vnexpress.net/nhung-loai-cu-qua-nen-an-thuong-xuyen-de-tang-mien-dich-4782034.html',
        'https://vnexpress.net/4-thoi-quen-an-uong-khien-hoi-tho-co-mui-4781725.html',
        'https://vnexpress.net/ngu-ngay-gay-hai-the-nao-4781321.html',
        'https://vnexpress.net/gia-vi-nao-ho-tro-thong-thoang-duong-tho-4781039.html',
        'https://vnexpress.net/nguyen-nhan-khien-phoi-lao-hoa-4780476.html',
        'https://vnexpress.net/bai-tap-nao-giup-giam-ngu-ngay-4780112.html',
        'https://vnexpress.net/thoi-quen-truoc-khi-ngu-tot-cho-ho-hap-4779874.html',
        'https://vnexpress.net/5-lam-tuong-ve-ngung-tho-khi-ngu-4779493.html',
        'https://vnexpress.net/thieu-ngu-tang-nguy-co-mac-benh-ho-hap-4779193.html',
        'https://vnexpress.net/bi-quyet-chay-bo-khong-kho-tho-4779096.html',
        'https://vnexpress.net/thoi-quen-nao-khien-phoi-dan-suy-kiet-4778737.html',
        'https://vnexpress.net/ve-sinh-phong-ngu-dung-cach-the-nao-4777867.html',
        'https://vnexpress.net/tran-dich-mang-phoi-4777406.html',
        'https://vnexpress.net/nghien-thuoc-la-bia-ruou-tang-nguy-co-ngung-tho-khi-ngu-4776181.html',
        'https://vnexpress.net/benh-lao-4775730.html',
        'https://vnexpress.net/dau-hieu-thieu-oxy-khi-ngu-4775720.html',
        'https://vnexpress.net/thuyen-tac-phoi-4773702.html',
        'https://vnexpress.net/10-cach-tang-kha-nang-mien-dich-cua-co-the-4773738.html',
        'https://vnexpress.net/cach-don-gian-thanh-loc-khong-khi-trong-nha-4773281.html',
        'https://vnexpress.net/an-gi-de-tang-mien-dich-it-om-vat-4773000.html',
        'https://vnexpress.net/khoi-bep-an-co-the-gay-benh-phoi-4772286.html',
        'https://vnexpress.net/an-nhieu-kem-uong-nuoc-da-de-benh-ho-hap-4771666.html',
        'https://vnexpress.net/trieu-chung-benh-bach-hau-khac-cam-covid-19-the-nao-4769080.html',
        'https://vnexpress.net/trieu-chung-benh-bach-hau-khac-cam-covid-19-the-nao-4769080.html',
        'https://vnexpress.net/5-thuc-pham-giup-giam-ngu-ngay-4769152.html',
        'https://vnexpress.net/cac-mon-an-co-the-hai-phoi-4768356.html',
        'https://vnexpress.net/6-mon-an-uong-bo-phoi-4766949.html',
        'https://vnexpress.net/nguoi-benh-hen-suyen-co-nen-uong-ca-phe-muoi-4766842.html',
        'https://vnexpress.net/nhung-dieu-it-biet-ve-phoi-4761992.html',
        'https://vnexpress.net/viem-phoi-do-nhiem-nam-4761139.html',
        'https://vnexpress.net/dau-hieu-nao-canh-bao-can-kham-phoi-4758672.html',
        'https://vnexpress.net/mang-phoi-san-sui-nhu-san-ho-do-ung-thu-di-can-4758010.html',
        'https://vnexpress.net/cham-soc-tre-so-sinh-viem-phoi-4757725.html',
        'https://vnexpress.net/tai-sao-phoi-suy-yeu-4755651.html',
        'https://vnexpress.net/tai-sao-viem-hong-de-bien-thanh-viem-phoi-4751230.html',
        'https://vnexpress.net/ngung-tho-khi-ngu-4750578.html',
        'https://vnexpress.net/lay-cum-trong-gia-dinh-ba-nguoi-nhap-vien-4750166.html',
        'https://vnexpress.net/hut-thuoc-la-hai-phoi-the-nao-4743290.html',
        'https://vnexpress.net/khong-hut-thuoc-nhieu-nguoi-van-mac-ung-thu-phoi-4737842.html',
        'https://vnexpress.net/nhieu-nguoi-nhap-vien-vi-cum-mua-bien-chung-viem-phoi-4737858.html',
        'https://vnexpress.net/kiem-tra-de-biet-ban-co-nguy-co-ung-thu-phoi-khong-4735062.html',
        'https://vnexpress.net/sot-ret-keo-dai-phat-hien-lao-mang-phoi-4732738.html',
        'https://vnexpress.net/cu-ong-nam-mot-cho-lau-ngay-bi-viem-phoi-loet-da-nang-4730575.html',
        'https://vnexpress.net/bien-chung-nguy-hiem-cua-cum-4726260.html',
        'https://vnexpress.net/ai-co-nguy-co-mac-benh-bui-phoi-4725881.html',
        'https://vnexpress.net/mac-thuy-dau-bien-chung-thanh-viem-phoi-4725419.html',
        'https://vnexpress.net/ho-ra-mau-o-at-do-gian-dong-mach-phe-quan-4724513.html',
        'https://vnexpress.net/mui-nen-thom-co-the-gay-benh-4719117.html',
        'https://vnexpress.net/tang-ap-phoi-tro-nang-khien-nguoi-phu-nu-ngat-xiu-4718196.html',
        'https://vnexpress.net/ap-xe-phoi-do-hoc-xuong-4715356.html',
        'https://vnexpress.net/dau-hieu-nhiem-virus-hop-bao-ho-hap-4714592.html',
        'https://vnexpress.net/viem-trang-phoi-sau-chuyen-leo-nui-4708745.html'
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
        with open('HoHapThuongGap.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
