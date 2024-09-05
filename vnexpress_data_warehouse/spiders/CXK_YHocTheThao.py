import scrapy
import csv

class CxkYhocthethaoSpider(scrapy.Spider):
    name = "CXK_YHocTheThao"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/ba-lam-tuong-thuong-gap-ve-phuc-hoi-chuc-nang-4778732.html',
                  'https://vnexpress.net/sau-an-bao-lau-co-the-chay-bo-4774852.html',
                  'https://vnexpress.net/meo-di-bo-giup-dot-chay-nhieu-calo-4763908.html',
                  'https://vnexpress.net/an-gi-truoc-va-sau-chay-bo-4761547.html',
                  'https://vnexpress.net/tai-sao-dau-that-lung-khi-chay-bo-4753611.html',
                  'https://vnexpress.net/nguy-co-dut-day-chang-o-nguoi-choi-the-thao-nghiep-du-4750167.html',
                  'https://vnexpress.net/5-meo-chay-bo-giam-can-nhanh-4747769.html',
                  'https://vnexpress.net/chay-bo-the-nao-de-giam-can-4744527.html',
                  'https://vnexpress.net/5-sai-lam-khi-chay-bo-gay-hai-xuong-khop-4737056.html',
                  'https://vnexpress.net/5-bai-tap-tang-suc-manh-co-bap-tay-4732800.html',
                  'https://vnexpress.net/chay-marathon-the-nao-khong-hai-xuong-khop-4732584.html',
                  'https://vnexpress.net/6-thoi-quen-giup-nguoi-trung-nien-khoe-xuong-khop-4731582.html',
                  'https://vnexpress.net/sau-mo-day-chang-bao-lau-co-the-choi-the-thao-4714520.html',
                  'https://vnexpress.net/tap-luyen-tro-lai-sau-tet-can-luu-y-gi-4712967.html',
                  'https://vnexpress.net/tai-sao-de-chan-thuong-khi-chay-bo-4704629.html',
                  'https://vnexpress.net/loi-ich-cua-nang-ta-voi-xuong-khop-4703252.html',
                  'https://vnexpress.net/ba-vi-tri-tren-co-the-de-chan-thuong-khi-tap-gym-4697638.html',
                  'https://vnexpress.net/loi-ich-voi-xuong-khop-khi-di-bo-nhanh-4697172.html',
                  'https://vnexpress.net/tap-hiit-giam-can-tang-co-4696353.html',
                  'https://vnexpress.net/nguy-co-thoai-hoa-khop-do-chan-thuong-the-thao-4694080.html',
                  'https://vnexpress.net/dau-hieu-canh-bao-ban-chay-bo-qua-suc-4693094.html',
                  'https://vnexpress.net/bai-tap-giam-can-tang-co-khong-can-den-phong-gym-4690643.html',
                  'https://vnexpress.net/lam-the-nao-chay-ben-khong-met-4689523.html',
                  'https://vnexpress.net/dau-hieu-mat-co-bap-4689282.html',
                  'https://vnexpress.net/dap-xe-tac-dong-den-co-the-the-nao-4685396.html',
                  'https://vnexpress.net/loi-ich-khi-tap-kick-boxing-4683950.html',
                  'https://vnexpress.net/loi-ich-khi-di-bo-buoi-sang-4682173.html',
                  'https://vnexpress.net/luu-y-cho-nguoi-lan-dau-chay-marathon-4681821.html',
                  'https://vnexpress.net/nhung-loi-tap-ta-de-mac-4680325.html',
                  'https://vnexpress.net/loi-ich-khi-nang-ta-nhe-4679155.html',
                  'https://vnexpress.net/co-nen-tap-ta-hang-ngay-de-tang-co-bap-4678393.html',
                  'https://vnexpress.net/co-nen-chay-bo-khi-troi-lanh-4676885.html',
                  'https://vnexpress.net/tap-pilates-tot-cho-xuong-khop-the-nao-4672222.html',
                  'https://vnexpress.net/loi-ich-khi-tap-luyen-voi-doi-chan-tran-4671813.html',
                  'https://vnexpress.net/loi-ich-khi-tap-plank-4671249.html',
                  'https://vnexpress.net/loi-ich-khi-di-bo-lui-4670451.html',
                  'https://vnexpress.net/ly-do-dau-xoc-hong-khi-tap-the-duc-4669894.html',
                  'https://vnexpress.net/tai-sao-tap-the-duc-nhung-khong-do-mo-hoi-4663528.html',
                  'https://vnexpress.net/tai-sao-long-ban-chan-dau-khi-ban-chay-bo-tren-may-4662841.html',
                  'https://vnexpress.net/5-dong-tac-yoga-giup-ban-cang-gia-cang-deo-4660631.html',
                  'https://vnexpress.net/tai-sao-ban-nen-khoi-dong-truoc-khi-tap-luyen-4659852.html',
                  'https://vnexpress.net/ly-do-ban-nen-tap-the-duc-buoi-toi-4658203.html',
                  'https://vnexpress.net/ban-da-tap-squat-dung-cach-4654057.html',
                  'https://vnexpress.net/vi-sao-ban-thuong-nong-chan-khi-chay-bo-4652607.html',
                  'https://vnexpress.net/an-gi-giam-dau-co-sau-khi-tap-the-duc-4651423.html',
                  'https://vnexpress.net/chan-thuong-thuong-gap-khi-chay-bo-4651192.html',
                  'https://vnexpress.net/tap-hit-dat-bao-nhieu-lan-mot-ngay-4647731.html',
                  'https://vnexpress.net/sai-lam-khi-di-bo-tang-nguy-co-chan-thuong-4646574.html',
                  'https://vnexpress.net/dap-xe-co-lam-to-bap-chan-4643568.html',
                  'https://vnexpress.net/chay-duoi-nuoc-mon-the-thao-co-loi-cho-xuong-khop-4643327.html',
                  'https://vnexpress.net/trac-nghiem-chon-mon-the-thao-tot-cho-xuong-khop-4634156.html',
                  'https://vnexpress.net/vi-sao-dau-dau-sau-khi-tap-the-duc-4632139.html',
                  'https://vnexpress.net/cach-chon-giay-chay-bo-phu-hop-4629398.html',
                  'https://vnexpress.net/cac-bai-tap-yoga-giup-lung-thang-4626339.html']

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
        with open('CXK_YHocTheThao.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

