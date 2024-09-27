import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import crawler_utils

class VnexpressDataWarehouseItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    disease_name = scrapy.Field()
    count_comments = scrapy.Field()
    total_like = scrapy.Field()
    content = scrapy.Field()

class TongHop_benhTMH(scrapy.Spider):
    name = "TongHop_benhTimMach"
    allowed_domains = ["vnexpress.net"]
    base_url1 = "https://vnexpress.net/suc-khoe/cac-benh/benh-tim-mach/benh-tre-em"
    base_url2 = "https://vnexpress.net/suc-khoe/cac-benh/benh-tim-mach/benh-nguoi-lon"

    start_urls1 = crawler_utils.crawl_articles(base_url1)
    start_urls2 = crawler_utils.crawl_articles(base_url2)

    start_urls = start_urls1 + start_urls2

    def __init__(self, *args, **kwargs):
        super(TongHop_benhTMH, self).__init__(*args, **kwargs)
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
            with open('TongHop_benhTimMach.csv', 'r', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open('TongHop_benhTimMach.csv', 'a', newline='', encoding='utf-8') as csvfile:
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