import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

class VnexpressDataWarehouseItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    disease_name = scrapy.Field()
    count_comments = scrapy.Field()
    total_like = scrapy.Field()
    content = scrapy.Field()

class TonghopBenhDLSpider(scrapy.Spider):
    name = "DaLieuCrawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/tram-cam-do-vay-nen-4797650.html",
        "https://vnexpress.net/hoi-nach-co-lay-khong-4739441.html",
        "https://vnexpress.net/nhieu-nguoi-nhiem-nam-viem-da-mua-mua-4785838.html",
        "https://vnexpress.net/dau-hieu-nhiem-giun-san-tren-da-4784809.html",
        "https://vnexpress.net/cach-nao-dieu-tri-nhanh-mun-trung-ca-4784321.html",
        "https://vnexpress.net/nguyen-nhan-gay-mui-co-the-4794609.html",
        "https://vnexpress.net/nhung-vung-da-thuong-bi-bo-quen-thoa-khi-kem-chong-nang-4782531.html",
        "https://vnexpress.net/goi-dau-bao-nhieu-lan-moi-tuan-4790166.html",
        "https://vnexpress.net/doc-kien-ba-khoang-nguy-hiem-the-nao-4789641.html",
        "https://vnexpress.net/loi-ich-khi-tam-nuoc-lanh-4781358.html",
        "https://vnexpress.net/co-nen-dung-don-thuoc-chua-mun-trung-ca-cua-nguoi-khac-4788048.html",
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
        "https://vnexpress.net/tai-sao-tuoi-thieu-nien-da-bac-toc-som-4743389.html",
        "https://vnexpress.net/bon-sai-lam-khi-dieu-tri-ung-thu-da-4757393.html",
        "https://vnexpress.net/hoa-chat-tay-rua-gay-kich-ung-viem-da-to-dia-4756504.html",
        "https://vnexpress.net/nguoi-tre-tim-cach-chua-rung-toc-4753686.html",
        "https://vnexpress.net/9-cach-giup-toc-nhanh-moc-4748645.html",
        "https://vnexpress.net/lam-gi-khi-moc-mun-noi-tiet-to-4741041.html",
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
        "https://vnexpress.net/nguyen-nhan-gay-tang-tiet-mo-hoi-4774310.html",
        "https://vnexpress.net/bien-chung-do-tu-dieu-tri-mun-4781466.html",
        "https://vnexpress.net/au-trung-di-chuyen-ngoan-ngoeo-duoi-da-chang-trai-4782410.html",
        "https://vnexpress.net/12-tuoi-co-triet-mo-hoi-nach-vinh-vien-duoc-khong-4737789.html",
        "https://vnexpress.net/thuoc-gia-truyen-khien-benh-vay-nen-bung-phat-4735907.html",
        "https://vnexpress.net/ngo-doc-anh-nang-mat-troi-4734372.html",
        "https://vnexpress.net/5-do-uong-khien-ban-nhanh-gia-4733825.html",
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
        "https://vnexpress.net/sui-mao-ga-nguy-hiem-the-nao-4599443.html",
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
        "https://vnexpress.net/triet-long-co-hieu-qua-vinh-vien-khong-4714122.html",
        ]
        
    def __init__(self, *args, **kwargs):
        super(TonghopBenhDLSpider, self).__init__(*args, **kwargs)
        # Khởi tạo Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        # Dùng Selenium để mở trang
        self.driver.get(response.url)
        # Đợi trang tải hoàn toàn (tối đa 10 giây)
        self.driver.implicitly_wait(10)

        # Tạo item
        item = VnexpressDataWarehouseItem()
        item['title'] = response.css('h1.title-detail::text').get(default='N/A')
        item['author'] = response.css('div.sidebar-1 > article.fck_detail  > p.Normal:last-child > strong::text').get(default='N/A')
        item['date'] = response.css('span.date::text').get(default='N/A')
        item['location'] = response.css('span.location-stamp::text').get(default='N/A')
        item['disease_name'] = response.css('body > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > ul > li:nth-child(3) > a::text').get(default='N/A')

        # Dùng Selenium để lấy số lượng bình luận
        try:
            item['count_comments'] = self.driver.find_element("xpath", '//*[@id="total_comment"]').text.strip() if self.driver.find_elements("xpath", '//*[@id="total_comment"]') else '0'
        except:
            item['count_comments'] = '0'

        # Dùng Selenium để tính tổng số "like"
        try:
            likes_elements = self.driver.find_elements("css selector", '#list_comment > div > div.content-comment > div > div > div.reactions-total > a.number')
            item['total_like'] = sum(int(element.text.strip()) for element in likes_elements)
        except:
            item['total_like'] = '0'
            
        item['content'] = ''.join(response.css('article.fck_detail p::text').getall())

        # Lưu dữ liệu vào CSV
        file_exists = False
        try:
            with open('TongHopDaLieu.csv', 'r', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open('TongHopDaLieu.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'author', 'date', 'location', 'disease_name', 'count_comments', 'total_like', 'content']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(item)

        # Tự động đi đến trang tiếp theo nếu có
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def close_spider(self, spider):
        # Đóng Selenium WebDriver khi spider dừng
        self.driver.quit()
