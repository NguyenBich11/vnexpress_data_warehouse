import scrapy
import csv


class ThammydacrawlerSpider(scrapy.Spider):
    name = "ThamMyDaCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/xoa-hinh-xam-nhieu-mau-bang-loai-laser-nao-4789281.html",
        "https://vnexpress.net/5-cach-ngan-seo-loi-phat-trien-4788890.html",
        "https://vnexpress.net/peel-da-bao-lau-la-du-4788041.html",
        "https://vnexpress.net/rui-ro-khi-tiem-filler-sai-cach-4787655.html",
        "https://vnexpress.net/luu-y-truoc-khi-triet-long-vinh-vien-4787438.html",
        "https://vnexpress.net/nhung-vi-tri-tren-mat-co-the-tiem-filler-4786504.html",
        "https://vnexpress.net/5-cach-thu-nho-lo-chan-long-4782138.html",
        "https://vnexpress.net/nhung-tinh-chat-dien-di-lam-dep-pho-bien-4780597.html",
        "https://vnexpress.net/xoa-nep-nhan-tran-bang-botox-the-nao-4780152.html",
        "https://vnexpress.net/phuong-phap-lam-dep-voi-axit-tca-4779927.html",
        "https://vnexpress.net/duong-chat-tu-nhien-giup-giam-ran-da-4778643.html",
        "https://vnexpress.net/dien-di-tre-hoa-da-nhu-the-nao-4776131.html",
        "https://vnexpress.net/cach-giam-bong-tham-mat-4775184.html",
        "https://vnexpress.net/5-tac-dung-lan-kim-voi-da-va-toc-4774647.html",
        "https://vnexpress.net/cach-cham-soc-vung-da-co-nguc-4772893.html",
        "https://vnexpress.net/triet-long-co-hieu-qua-bao-lau-4772368.html",
        "https://vnexpress.net/co-nen-truyen-chat-trang-da-4772312.html",
        "https://vnexpress.net/phuong-phap-xoa-nong-cam-doi-4771734.html",
        "https://vnexpress.net/tai-sao-nam-noi-tiet-kho-dieu-tri-4769157.html",
        "https://vnexpress.net/nhung-dieu-can-biet-ve-tiem-meso-4768668.html",
        "https://vnexpress.net/phuong-phap-nao-dieu-tri-seo-4767428.html",
        "https://vnexpress.net/co-nen-dap-mat-na-qua-dem-4767056.html",
        "https://vnexpress.net/tiem-botox-dieu-tri-cuoi-ho-loi-nhu-the-nao-4765960.html",
        "https://vnexpress.net/thac-mac-thuong-gap-khi-xoa-hinh-xam-4765584.html",
        "https://vnexpress.net/dau-hieu-lao-hoa-da-de-nhan-biet-4765259.html",
        "https://vnexpress.net/dung-tia-laser-xoa-not-ruoi-mi-mat-4764677.html",
        "https://vnexpress.net/dap-mat-bang-vo-chuoi-co-giup-trang-da-4763979.html",
        "https://vnexpress.net/lam-gi-khi-tiem-filler-bi-von-cuc-4763975.html",
        "https://vnexpress.net/tri-lieu-da-bang-cong-nghe-cao-hut-khach-dip-he-4762870.html",
        "https://vnexpress.net/tai-sao-tiem-filler-o-ma-bi-von-cuc-4761267.html",
        "https://vnexpress.net/cac-loai-seo-thuong-gap-4759267.html",
        "https://vnexpress.net/nen-triet-long-vung-kin-bang-phuong-phap-nao-4758496.html",
        "https://vnexpress.net/tiem-filler-lam-dep-duoc-bao-lau-4756986.html",
        "https://vnexpress.net/xoa-xam-co-de-lai-seo-4756059.html",
        "https://vnexpress.net/co-nen-xong-hoi-mat-bang-nuoc-nong-moi-ngay-4755865.html",
        "https://vnexpress.net/dot-not-ruoi-bang-laser-ngan-hoa-ung-thu-4755507.html",
        "https://vnexpress.net/co-nen-tu-peel-da-nach-4755046.html",
        "https://vnexpress.net/thu-pham-gay-nam-da-4754619.html",
        "https://vnexpress.net/cach-cham-soc-vet-thuong-tranh-seo-4754131.html",
        "https://vnexpress.net/song-sieu-am-co-giup-giam-beo-4752272.html",
        "https://vnexpress.net/nen-triet-long-hay-tri-hoi-nach-truoc-4751870.html",
        "https://vnexpress.net/bo-sung-collagen-cho-da-dung-cach-4751511.html",
        "https://vnexpress.net/loi-ich-cua-triet-long-4750045.html",
        "https://vnexpress.net/tay-te-bao-da-chet-bang-ba-ca-phe-4749140.html",
        "https://vnexpress.net/not-ruoi-sam-mau-ngua-co-phai-ung-thu-4747299.html",
        "https://vnexpress.net/xoa-bot-mau-ca-phe-sua-bang-laser-4741973.html",
        "https://vnexpress.net/cach-dieu-tri-tham-moi-4740477.html",
        "https://vnexpress.net/tai-sao-bi-bien-chung-sau-tiem-filler-4740141.html",
        "https://vnexpress.net/triet-long-co-het-hoi-nach-4736488.html",
        "https://vnexpress.net/tiem-botox-lam-dep-co-gay-doc-4732246.html",
        "https://vnexpress.net/tai-sao-tre-moi-sinh-co-vet-bot-4731737.html",
        "https://vnexpress.net/tac-dung-cua-tiem-ha-4731192.html",
        "https://vnexpress.net/tiem-botox-xoa-nhan-the-nao-4730559.html",
        "https://vnexpress.net/5-cach-tri-seo-ro-4729563.html",
        "https://vnexpress.net/nhieu-nguoi-triet-long-tri-mui-hoi-mua-nong-4727156.html",
        "https://vnexpress.net/cach-lam-thon-gon-ham-khong-can-phau-thuat-4721231.html",
        "https://vnexpress.net/ba-phuong-phap-nhanh-chong-tri-nam-da-4719059.html",
        "https://vnexpress.net/5-thuc-uong-chong-nang-cho-da-4718210.html",
        "https://vnexpress.net/ngu-tu-the-nao-de-co-lan-da-dep-4717648.html",
        "https://vnexpress.net/4-cong-thuc-mat-na-mo-tham-4717517.html",
        "https://vnexpress.net/an-gi-bo-sung-collagen-cho-da-4717114.html",
        "https://vnexpress.net/5-loai-mat-na-giam-nep-nhan-4714342.html",
        "https://vnexpress.net/triet-long-co-hieu-qua-vinh-vien-khong-4714122.html"
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
        with open('Data_ThamMyDa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        


