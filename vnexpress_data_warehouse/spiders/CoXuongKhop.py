import scrapy
import csv


class CoxuongkhopSpider(scrapy.Spider):
    name = "CoXuongKhop_NoiKhoa"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/ba-nhom-dinh-duong-trong-nuoc-ham-xuong-4787674.html',
                  'https://vnexpress.net/thoai-hoa-khop-hang-4787803.html',
                  'https://vnexpress.net/mac-viem-khop-co-duoc-an-trung-4786718.html',
                  'https://vnexpress.net/7-bai-tap-hang-ngay-giam-dau-khop-4786066.html',
                  'https://vnexpress.net/xet-nghiem-chan-doan-gout-the-nao-4786274.html',
                  'https://vnexpress.net/nhung-loai-rau-cu-giau-canxi-giup-xuong-chac-khoe-4785249.html',
                  'https://vnexpress.net/lieu-phap-nong-lanh-giup-giam-viem-khop-4784304.html',
                  'https://vnexpress.net/tinh-the-gout-hinh-thanh-the-nao-4784069.html',
                  'https://vnexpress.net/dong-cung-vai-canh-bao-viem-khop-4783639.html',
                  'https://vnexpress.net/nhung-nguoi-nen-tiem-chat-nhon-cho-khop-goi-4782536.html',
                  'https://vnexpress.net/bi-benh-gout-an-dua-duoc-khong-4780912.html',
                  'https://vnexpress.net/5-bai-tap-nen-luu-y-khi-thoai-hoa-khop-goi-4779893.html',
                  'https://vnexpress.net/thua-can-beo-phi-de-nang-xuong-khop-4779697.html',
                  'https://vnexpress.net/stress-lam-tang-nguy-co-mac-benh-gout-the-nao-4776537.html',
                  'https://vnexpress.net/thoai-hoa-khop-goi-co-chua-khoi-khong-4778170.html',
                  'https://vnexpress.net/nhung-thuc-pham-de-gay-yeu-xuong-khop-4777939.html',
                  'https://vnexpress.net/dau-long-ban-chan-khi-ngu-day-la-benh-gi-4776688.html',
                  'https://vnexpress.net/cach-giam-kho-cung-khop-4775689.html',
                  'https://vnexpress.net/tai-sao-phu-nu-de-mac-viem-khop-dang-thap-4775075.html',
                  'https://vnexpress.net/4-giai-doan-cua-benh-gout-4774233.html',
                  'https://vnexpress.net/thoai-hoa-khop-khac-viem-khop-dang-thap-the-nao-4773933.html',
                  'https://vnexpress.net/kho-gap-duoi-ngon-tay-canh-bao-viem-bao-gan-4773690.html',
                  'https://vnexpress.net/lam-dung-ruou-bia-huy-hoai-xuong-dui-4773008.html',
                  'https://vnexpress.net/benh-gout-co-di-truyen-khong-4772016.html',
                  'https://vnexpress.net/dau-hieu-thoai-hoa-khop-goi-theo-tung-giai-doan-4771268.html',
                  'https://vnexpress.net/meo-ngu-ngon-cho-nguoi-benh-viem-khop-dang-thap-4770062.html',
                  'https://vnexpress.net/6-bai-tap-tot-cho-nguoi-thoai-hoa-khop-goi-4769192.html',
                  'https://vnexpress.net/5-hoat-dong-nguoi-benh-thoai-hoa-khop-goi-nen-tranh-4767998.html',
                  'https://vnexpress.net/suyt-tan-phe-do-lo-la-chua-gout-4767567.html',
                  'https://vnexpress.net/dau-bap-co-tot-cho-xuong-khop-4766795.html',
                  'https://vnexpress.net/12-benh-co-dau-hieu-te-bi-tay-chan-4764764.html',
                  'https://vnexpress.net/khi-nao-nen-tiem-chat-nhon-cho-khop-goi-4763264.html',
                  'https://vnexpress.net/nguyen-nhan-nao-gay-tang-axit-uric-4761786.html',
                  'https://vnexpress.net/nguyen-nhan-thuong-gap-gay-thoai-hoa-khop-4760491.html',
                  'https://vnexpress.net/uong-ruou-bia-gay-hai-xuong-the-nao-4761080.html',
                  'https://vnexpress.net/e-am-dau-nhuc-xuong-khop-canh-bao-benh-gi-4758494.html',
                  'https://vnexpress.net/dau-nhuc-khop-hang-canh-bao-hoai-tu-chom-xuong-dui-4757294.html',
                  'https://vnexpress.net/4-giai-doan-thoai-hoa-khop-4756072.html',
                  'https://vnexpress.net/hai-chan-veo-45-do-do-thoai-hoa-khop-goi-4755700.html',
                  'https://vnexpress.net/nguoi-benh-thoat-vi-dia-dem-nen-an-gi-4755001.html',
                  'https://vnexpress.net/phan-biet-benh-gout-va-gia-gout-4751115.html',
                  'https://vnexpress.net/lam-tuong-ve-thuc-pham-gay-viem-khop-4749578.html',
                  'https://vnexpress.net/nhung-phuong-phap-hien-dai-dieu-tri-thoai-hoa-khop-goi-4749211.html',
                  'https://vnexpress.net/het-dau-sau-10-nam-mac-benh-khop-hang-4748198.html',
                  'https://vnexpress.net/ung-dung-tri-tue-nhan-tao-chan-doan-loang-xuong-4747702.html',
                  'https://vnexpress.net/cach-chon-giay-cho-nguoi-viem-khop-ban-chan-4746480.html',
                  'https://vnexpress.net/chay-bo-co-gay-thoai-hoa-khop-goi-4746675.html',
                  'https://vnexpress.net/viem-khop-co-the-gay-tan-tat-khong-4745345.html',
                  'https://vnexpress.net/khop-nao-de-bi-thoai-hoa-4743645.html',
                  'https://vnexpress.net/nguy-co-ton-thuong-gan-co-tay-do-nghien-smartphone-4743939.html',
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
        with open('CoXuongKhop_NoiKhoa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
