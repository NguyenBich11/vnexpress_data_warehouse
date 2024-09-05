import scrapy
import csv


class BenhdalieucrawlerPySpider(scrapy.Spider):
    name = "BenhDaLieuCrawler.py"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/co-nen-dung-don-thuoc-chua-mun-trung-ca-cua-nguoi-khac-4788048.html",
        "https://vnexpress.net/5-lam-tuong-ve-mun-4786114.html",
        "https://vnexpress.net/nhieu-nguoi-nhiem-nam-viem-da-mua-mua-4785838.html",
        "https://vnexpress.net/do-mo-hoi-uot-ao-du-o-phong-dieu-hoa-la-benh-gi-4785376.html",
        "https://vnexpress.net/dau-hieu-nhiem-giun-san-tren-da-4784809.html",
        "https://vnexpress.net/cach-nao-dieu-tri-nhanh-mun-trung-ca-4784321.html",
        "https://vnexpress.net/6-rau-cu-tre-hoa-da-4783976.html",
        "https://vnexpress.net/7-thoi-quen-hang-ngay-khien-da-lao-hoa-som-4783481.html",
        "https://vnexpress.net/nhung-vung-da-thuong-bi-bo-quen-thoa-khi-kem-chong-nang-4782531.html",
        "https://vnexpress.net/au-trung-di-chuyen-ngoan-ngoeo-duoi-da-chang-trai-4782410.html",
        "https://vnexpress.net/bien-chung-do-tu-dieu-tri-mun-4781466.html",
        "https://vnexpress.net/loi-ich-khi-tam-nuoc-lanh-4781358.html",
        "https://vnexpress.net/ly-do-khong-nen-de-toc-uot-di-ngu-4779573.html",
        "https://vnexpress.net/10-nam-chua-mun-trung-ca-4779178.html",
        "https://vnexpress.net/4-chuc-nang-cua-da-4778428.html",
        "https://vnexpress.net/dieu-tri-vay-nen-bang-thuoc-sinh-hoc-4777793.html",
        "https://vnexpress.net/meo-xoa-sach-mun-lung-4777309.html",
        "https://vnexpress.net/bong-doc-kien-ba-khoang-vao-mua-mua-4776963.html",
        "https://vnexpress.net/bien-chung-nguy-hiem-cua-benh-vay-nen-4776531.html",
        "https://vnexpress.net/nguyen-nhan-gay-tang-tiet-mo-hoi-4774310.html",
        "https://vnexpress.net/seo-hinh-thanh-nhu-the-nao-4773985.html",
        "https://vnexpress.net/cach-hap-thu-vitamin-d-an-toan-khi-phoi-nang-4773588.html",
        "https://vnexpress.net/ruou-anh-huong-den-benh-vay-nen-the-nao-4773188.html",
        "https://vnexpress.net/lam-the-nao-het-mun-dau-den-4771026.html",
        "https://vnexpress.net/10-nguyen-nhan-gay-mun-trung-ca-4770174.html",
        "https://vnexpress.net/ai-de-bi-tan-nhang-4769590.html",
        "https://vnexpress.net/khi-nao-can-dieu-tri-mun-4769519.html",
        "https://vnexpress.net/kem-chong-nang-vat-ly-khac-kem-hoa-hoc-the-nao-4768199.html",
        "https://vnexpress.net/co-the-chua-khoi-vay-nen-khong-4767757.html",
        "https://vnexpress.net/cach-dung-kem-chong-nang-dang-xit-hieu-qua-4766389.html",
        "https://vnexpress.net/cach-cham-soc-da-vay-nen-4763655.html",
        "https://vnexpress.net/bi-viem-da-di-ung-nen-an-gi-4762341.html",
        "https://vnexpress.net/an-gi-giup-da-hoi-phuc-sau-chay-nang-4762308.html",
        "https://vnexpress.net/me-day-4761817.html",
        "https://vnexpress.net/chan-doan-dieu-tri-not-ruoi-ung-thu-the-nao-4760602.html",
        "https://vnexpress.net/tiem-huyet-tuong-giau-tieu-cau-chua-rung-toc-the-nao-4760155.html",
        "https://vnexpress.net/nhung-bien-chung-da-thuong-gap-do-my-pham-4759687.html",
        "https://vnexpress.net/meo-chong-nang-khi-di-may-bay-4758793.html",
        "https://vnexpress.net/viem-da-co-dia-benh-de-tai-phat-khi-giao-mua-4758194.html",
        "https://vnexpress.net/toc-rung-bao-nhieu-soi-moi-dang-lo-4757837.html",
        "https://vnexpress.net/bon-sai-lam-khi-dieu-tri-ung-thu-da-4757393.html",
        "https://vnexpress.net/hoa-chat-tay-rua-gay-kich-ung-viem-da-to-dia-4756504.html",
        "https://vnexpress.net/nguoi-tre-tim-cach-chua-rung-toc-4753686.html",
        "https://vnexpress.net/9-cach-giup-toc-nhanh-moc-4748645.html",
        "https://vnexpress.net/trieu-chung-nao-nhan-biet-vay-nen-4751024.html",
        "https://vnexpress.net/co-nen-trang-diem-ngay-nang-nong-4750494.html",
        "https://vnexpress.net/laser-tri-nam-da-nhu-the-nao-4749624.html",
        "https://vnexpress.net/hai-kieu-rung-toc-o-phu-nu-4748650.html",
        "https://vnexpress.net/nhung-van-de-da-thuong-gap-vao-mua-he-4748238.html",
        "https://vnexpress.net/noi-me-day-boi-di-ung-thuc-an-4747518.html",
        "https://vnexpress.net/co-kieng-tiep-xuc-khi-mac-benh-zona-4746696.html",
        "https://vnexpress.net/phan-biet-trieu-chung-zona-va-kien-ba-khoang-tren-da-4746377.html",
        "https://vnexpress.net/co-nen-nho-toc-bac-toc-sau-4745810.html",
        "https://vnexpress.net/nang-nong-hai-da-the-nao-4745392.html",
        "https://vnexpress.net/mac-quan-ao-moi-chua-giat-co-lay-benh-4744885.html",
        "https://vnexpress.net/soc-xuat-hien-o-mong-tay-la-benh-gi-4744780.html",
        "https://vnexpress.net/tam-rua-bang-nuoc-am-co-tot-cho-da-4744345.html",
        "https://vnexpress.net/nguy-hiem-khi-chua-zona-bang-meo-dan-gian-4743822.html",
        "https://vnexpress.net/8-mon-giau-vitamin-giup-da-dep-toc-khoe-4743423.html",
        "https://vnexpress.net/tai-sao-tuoi-thieu-nien-da-bac-toc-som-4743389.html",
        "https://vnexpress.net/6-van-de-suc-khoe-bieu-hien-qua-mai-toc-4742415.html",
        "https://vnexpress.net/6-benh-gay-rung-toc-4739662.html"
        ]

    def parse(self, response):
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('Data_BenhDaLieu.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        

