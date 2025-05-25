import scrapy
from vnexpress_data_warehouse.items import VnexpressDataWarehouseItem 

class BenhtimmachSpider(scrapy.Spider):
    name = "BenhTimMach"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/nhan-giap-tien-trien-ung-thu-4785610.html',
        'https://vnexpress.net/cuong-giap-loi-mat-do-benh-basedow-4784710.html',
        'https://vnexpress.net/tuong-mac-benh-tam-ly-hoa-cuong-giap-4784388.html',
        'https://vnexpress.net/buou-co-to-gay-kho-tho-4783549.html',
        'https://vnexpress.net/bach-cau-giam-manh-do-tac-dung-phu-cua-thuoc-chua-cuong-giap-4759724.html',
        'https://vnexpress.net/co-phinh-to-boi-nang-giap-4741323.html',
        'https://vnexpress.net/kham-suc-khoe-dinh-ky-phat-hien-ung-thu-tuyen-giap-4726805.html',
        'https://vnexpress.net/bat-ngo-phat-hien-ung-thu-khi-kham-suc-khoe-4725670.html',
        'https://vnexpress.net/u-tuyen-giap-lanh-tinh-hoa-ung-thu-sau-10-nam-4702762.html',
        'https://vnexpress.net/phat-hien-cuong-giap-tu-dau-hieu-kho-tho-tim-dap-nhanh-4700814.html',
        'https://vnexpress.net/suy-tim-do-cuong-giap-ma-khong-biet-4690458.html',
        'https://vnexpress.net/tuong-benh-tuoi-gia-hoa-cuong-giap-bien-chung-tim-4688789.html',
        'https://vnexpress.net/dot-ngot-noi-ngong-do-suy-giap-4685997.html',
        'https://vnexpress.net/kho-tho-boi-buou-co-khong-lo-4676134.html',
        'https://vnexpress.net/cuong-giap-khien-nguoi-dan-ong-liet-hai-chan-4669409.html',
        'https://vnexpress.net/tuong-dot-quy-hoa-u-tuyen-thuong-than-4653156.html',
        'https://vnexpress.net/suy-tim-do-giam-hormone-tuyen-giap-4644868.html',
        'https://vnexpress.net/tuong-sut-can-hoa-cuong-giap-nang-4638161.html',
        'https://vnexpress.net/phat-hien-benh-tuyen-giap-khi-kham-tim-4637591.html',
        'https://vnexpress.net/suy-giap-sau-10-nam-cat-tuyen-giap-4633800.html',
        'https://vnexpress.net/khoi-u-moc-chan-xam-lan-tuyen-giap-4622278.html',
        'https://vnexpress.net/roi-loan-nhip-tim-do-quen-uong-thuoc-tri-benh-tuyen-giap-4609253.html',
        'https://vnexpress.net/cuu-co-gai-19-tuoi-khoi-suy-tim-do-cuong-giap-4608376.html',
        'https://vnexpress.net/loan-nhip-tim-khien-nguoi-benh-cuong-giap-nguy-kich-4505434.html',
        'https://vnexpress.net/mo-buou-giap-ac-tinh-cho-benh-nhan-beo-phi-4496844.html',
        'https://vnexpress.net/cuong-giap-suy-gan-nang-o-benh-nhan-tieu-duong-4467644.html',
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
        "https://vnexpress.net/kem-chong-nang-vat-ly-khac-kem-hoa-hoc-the-nao-4768199.html"]

    def parse(self, response):
        item = VnexpressDataWarehouseItem()
        #'article_id': response.css('meta[property="og:url"]::attr(content)').get(default='N/A').split('/')[-1],
        item['title'] = response.css('h1.title-detail::text').get(default='N/A')
        item['author'] = response.css('div.sidebar-1 > article.fck_detail  > p.Normal:last-child > strong::text').get(default='N/A')
        item['date'] = response.css('span.date::text').get(default='N/A')
        item['location'] = response.css('span.location-stamp::text').get()
        item['disease_name'] = response.css('body > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > ul > li:nth-child(3) > a::text').get()
        item['count_comment'] = response.css('label #total_comment::text').get(default='N/A')
        item['total_like'] = response.css('#list_comment > div > div.content-comment > div > div > div.reactions-total > a.number::text').get(default='N/A')
        item['content'] = ''.join(response.css('article.fck_detail p::text').getall())
        yield item

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
