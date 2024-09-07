import csv
import scrapy

class DemoBvtSpider(scrapy.Spider):
    name = "Demo_BVT"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/u-tai-do-thung-mang-nhi-4786434.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-co-the-chua-khoi-khong-4783817.html',
                  'https://vnexpress.net/nhung-thoi-quen-gay-suy-giam-thinh-luc-4779660.html',
                  'https://vnexpress.net/do-nhi-luong-de-lam-gi-4771858.html',
                  'https://vnexpress.net/viem-tai-giua-4772425.html',
                  'https://vnexpress.net/nhung-benh-thuong-gap-o-dai-tai-4782611.html',
                  'https://vnexpress.net/hoa-mat-chong-mat-la-dau-hieu-roi-loan-tien-dinh-4753501.html',
                  'https://vnexpress.net/chong-mat-tu-the-kich-phat-lanh-tinh-4748520.html',
                  'https://vnexpress.net/nguy-co-giam-thinh-luc-do-deo-tai-nghe-am-luong-lon-4747235.html',
                  'https://vnexpress.net/ret-chui-vao-tai-chang-trai-can-thung-mang-nhi-4725632.html',
                  'https://vnexpress.net/nhieu-nguoi-viem-tai-sau-di-boi-giai-nhiet-4721376.html',
                  'https://vnexpress.net/an-gi-giup-ban-nghe-tot-hon-4719908.html',
                  'https://vnexpress.net/sai-lam-gay-hai-cho-tai-4714452.html',
                  'https://vnexpress.net/thung-mang-nhi-boi-tieng-phao-no-4713105.html',
                  'https://vnexpress.net/tre-viem-tai-giua-co-nen-di-may-bay-4708982.html',
                  'https://vnexpress.net/meo-chong-say-tau-xe-ngay-tet-4708968.html',
                  'https://vnexpress.net/deo-tai-nghe-co-giam-say-tau-xe-4708738.html',
                  'https://vnexpress.net/bo-dieu-tri-roi-loan-tien-dinh-nang-4707644.html',
                  'https://vnexpress.net/diec-mot-ben-tai-co-chua-khoi-duoc-khong-4706203.html',
                  'https://vnexpress.net/nguyen-nhan-gay-tieng-keu-tach-tach-trong-tai-4703501.html',
                  'https://vnexpress.net/loi-ich-khi-massage-tai-4703041.html',
                  'https://vnexpress.net/nhung-dang-roi-loan-tien-dinh-thuong-gap-4702625.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-ma-khong-biet-4699428.html',
                  'https://vnexpress.net/viem-tai-xuong-chum-4696311.html',
                  'https://vnexpress.net/cach-giam-u-tai-khi-ngoi-may-bay-4694812.html',
                  'https://vnexpress.net/tuong-quai-bi-hoa-u-tuyen-mang-tai-4691727.html',
                  'https://vnexpress.net/ly-do-khong-nen-ngoay-tai-4690725.html',
                  'https://vnexpress.net/nam-ong-tai-ngoai-co-tu-khoi-4685199.html',
                  'https://vnexpress.net/tai-nghe-thanh-o-vi-khuan-khi-lau-ngay-khong-ve-sinh-4683244.html',
                  'https://vnexpress.net/su-that-thu-vi-ve-tai-4682904.html',
                  'https://vnexpress.net/viem-tai-giua-co-tu-khoi-khong-4679492.html',
                  'https://vnexpress.net/nhieu-hat-cat-li-ti-trong-tai-be-trai-4673383.html',
                  'https://vnexpress.net/nguyen-nhan-tai-chay-mau-4668710.html',
                  'https://vnexpress.net/dau-hieu-bat-thuong-o-tai-canh-bao-benh-4667390.html',
                  'https://vnexpress.net/nguyen-nhan-khien-tai-co-mui-kho-chiu-4667064.html',
                  'https://vnexpress.net/tieng-on-anh-huong-den-tai-the-nao-4665938.html',
                  'https://vnexpress.net/bac-si-viet-va-maylaysia-trinh-dien-cay-oc-tai-benh-nhan-4664853.html',
                  'https://vnexpress.net/6-thuc-pham-khong-tot-cho-nguoi-roi-loan-tien-dinh-4662012.html',
                  'https://vnexpress.net/lam-gi-khi-bi-roi-loan-tien-dinh-4660749.html',
                  'https://vnexpress.net/bao-ve-tai-nhu-the-nao-4658769.html',
                  'https://vnexpress.net/nguyen-nhan-u-tai-keo-dai-4658171.html',
                  'https://vnexpress.net/viem-tai-giua-lam-thung-mang-nhi-4657600.html',
                  'https://vnexpress.net/an-gi-giam-roi-loan-tien-dinh-4657007.html',
                  'https://vnexpress.net/sai-lam-khi-dung-tai-nghe-4656614.html',
                  'https://vnexpress.net/thung-mang-nhi-boi-chiec-tam-bong-ngoay-tai-4655936.html',
                  'https://vnexpress.net/doan-benh-qua-mau-ray-tai-4653682.html',
                  'https://vnexpress.net/nguyen-nhan-tich-tu-ray-tai-4652578.html',
                  'https://vnexpress.net/vi-sao-khong-nen-deo-tai-nghe-khi-ngu-4646592.html',
                  'https://vnexpress.net/nut-ray-4-cm-bit-kin-hai-tai-be-trai-4646171.html',
                  'https://vnexpress.net/viem-tai-xuong-chum-4643833.html',
                  'https://vnexpress.net/nhiem-trung-tai-do-nam-4641430.html',
                  'https://vnexpress.net/6-cach-giam-tac-tai-4640485.html',
                  'https://vnexpress.net/chong-mat-buon-non-trieu-chung-roi-loan-tien-dinh-4636237.html',
                  'https://vnexpress.net/khi-nao-can-tham-kham-nhiem-trung-tai-4628742.html',
                  'https://vnexpress.net/thung-mang-nhi-vi-nhiem-nam-ong-tai-4620633.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-nen-an-gi-kieng-gi-4620044.html',
                  'https://vnexpress.net/nguyen-nhan-gay-dau-ong-tai-4618315.html',
                  'https://vnexpress.net/cac-nguyen-nhan-gay-sung-tai-va-cach-dieu-tri-4616066.html',
                  'https://vnexpress.net/9-nguyen-nhan-gay-vay-trong-tai-4607599.html',
                  'https://vnexpress.net/xu-tri-the-nao-khi-kien-chui-vao-tai-4605776.html',
                  'https://vnexpress.net/5-bai-tap-cai-thien-chong-mat-do-roi-loan-tien-dinh-4599505.html',
                  'https://vnexpress.net/4-meo-giup-ngu-ngon-khi-bi-u-tai-4597235.html',
                  'https://vnexpress.net/cac-bien-chung-nguy-hiem-cua-nhiem-trung-tai-4595383.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-co-nen-uong-thuoc-bo-nao-4593772.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-co-gay-dot-quy-khong-4592020.html',
                  'https://vnexpress.net/tac-hai-khi-nhin-hat-hoi-4591683.html',
                  'https://vnexpress.net/cac-nguyen-nhan-gay-dau-tai-thuong-gap-4590884.html',
                  'https://vnexpress.net/5-benh-ly-khien-tai-dau-nhoi-4590553.html',
                  'https://vnexpress.net/ly-do-nghe-thay-tieng-mach-dap-trong-tai-4586987.html',
                  'https://vnexpress.net/nhung-phuong-phap-loai-bo-ray-tai-4585706.html',
                  'https://vnexpress.net/nhung-dong-tac-yoga-giup-giam-cac-benh-ve-tai-4585485.html',
                  'https://vnexpress.net/nhan-biet-chong-mat-do-roi-loan-tien-dinh-4584998.html',
                  'https://vnexpress.net/4-bien-chung-do-xo-lo-tai-4582203.html',
                  'https://vnexpress.net/nguyen-nhan-tai-bi-chay-mau-4581182.html',
                  'https://vnexpress.net/moi-nguy-khi-lay-ray-tai-bang-tam-bong-4574824.html',
                  'https://vnexpress.net/60-nguyen-nhan-gay-diec-bam-sinh-co-the-phong-ngua-4572719.html',
                  'https://vnexpress.net/khi-nao-can-dung-may-tro-thinh-4571769.html',
                  'https://vnexpress.net/dieu-nen-lam-nen-tranh-khi-chua-nhiem-trung-tai-4570561.html',
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
        with open('BenhVeTai.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)