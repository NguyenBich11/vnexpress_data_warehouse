import scrapy
import csv


class BenhstiscrawlerSpider(scrapy.Spider):
    name = "BenhSTIsCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/nhung-benh-tinh-duc-co-the-lay-qua-nu-hon-4783134.html",
        "https://vnexpress.net/tai-sao-dung-bao-cao-su-van-co-the-lay-benh-tinh-duc-4786939.html",
        "https://vnexpress.net/7-lam-tuong-ve-benh-tinh-duc-4777324.html",
        "https://vnexpress.net/hpv-co-lay-khi-hon-4775535.html",
        "https://vnexpress.net/mun-coc-sinh-duc-4766613.html",
        "https://vnexpress.net/cac-benh-tinh-duc-gay-trieu-chung-giong-cum-4770334.html",
        "https://vnexpress.net/ly-do-nen-xet-nghiem-benh-tinh-duc-4743891.html",
        "https://vnexpress.net/5-trieu-chung-canh-bao-benh-tinh-duc-o-nam-gioi-4763239.html",
        "https://vnexpress.net/tai-sao-khong-quan-he-ngoai-luong-van-nhiem-benh-tinh-duc-4752662.html",
        "https://vnexpress.net/dau-hieu-benh-tinh-duc-o-nam-gioi-4747782.html",
        "https://vnexpress.net/vo-chong-chung-thuy-sao-van-mac-giang-mai-4743086.html",
        "https://vnexpress.net/ran-mu-4741780.html",
        "https://vnexpress.net/nhung-benh-tinh-duc-co-the-lay-truyen-qua-da-4741528.html",
        "https://vnexpress.net/benh-tinh-duc-nao-co-the-tai-nhiem-4736785.html",
        "https://vnexpress.net/cac-benh-tinh-duc-co-the-truyen-tu-me-sang-con-4733275.html",
        "https://vnexpress.net/tai-nhiem-giang-mai-khi-quan-he-dong-gioi-4732902.html",
        "https://vnexpress.net/lam-gi-khi-nhiem-hpv-4730428.html",
        "https://vnexpress.net/dau-hieu-canh-bao-giang-mai-4728592.html",
        "https://vnexpress.net/hpv-duoc-chan-doan-nhu-the-nao-4722550.html",
        "https://vnexpress.net/nhung-lam-tuong-thuong-gap-ve-hpv-4719413.html",
        "https://vnexpress.net/bat-ngo-phat-hien-giang-mai-khi-san-con-tuoi-rong-4708297.html",
        "https://vnexpress.net/nhung-benh-tinh-duc-co-the-gay-dau-hong-4702431.html",
        "https://vnexpress.net/dau-hieu-mac-benh-lau-4700143.html",
        "https://vnexpress.net/dau-hieu-nhan-biet-benh-tinh-duc-va-nhiem-trung-tiet-nieu-4654553.html",
        "https://vnexpress.net/vi-sao-benh-giang-mai-kho-phat-hien-4659843.html",
        "https://vnexpress.net/giang-mai-benh-tinh-duc-lam-giam-kha-nang-co-thai-4658528.html",
        "https://vnexpress.net/hon-co-lay-benh-tinh-duc-4646388.html",
        "https://vnexpress.net/mun-rop-sinh-duc-co-tai-phat-sau-dieu-tri-4642557.html",
        "https://vnexpress.net/mun-mem-o-vung-kin-la-benh-gi-4635681.html",
        "https://vnexpress.net/te-cung-chan-do-mac-giang-mai-4635529.html",
        "https://vnexpress.net/di-tieu-rat-phat-hien-benh-lau-4632746.html",
        "https://vnexpress.net/mat-ngu-vi-ran-mu-lam-to-vung-kin-4631945.html",
        "https://vnexpress.net/dau-hieu-thuong-gap-cua-benh-lau-4623369.html",
        "https://vnexpress.net/phan-biet-u-nhu-sinh-duc-va-sui-mao-ga-4621516.html",
        "https://vnexpress.net/4-bien-chung-nguy-hiem-cua-giang-mai-4618518.html",
        "https://vnexpress.net/tai-sao-khong-quan-he-van-co-the-mac-benh-tinh-duc-4605303.html",
        "https://vnexpress.net/cac-benh-nhiem-trung-lay-qua-duong-tinh-duc-4608499.html",
        "https://vnexpress.net/nhung-bien-chung-nguy-hiem-cua-benh-lau-4599514.html",
        "https://vnexpress.net/can-benh-am-tham-gay-vo-sinh-o-ca-nam-va-nu-4599499.html",
        "https://vnexpress.net/6-dieu-it-biet-ve-mun-rop-sinh-duc-4599449.html",
        "https://vnexpress.net/sui-mao-ga-nguy-hiem-the-nao-4599443.html"
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
        with open('Data_BenhSTIs.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)        


