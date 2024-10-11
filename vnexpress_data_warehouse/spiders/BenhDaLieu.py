import scrapy
from vnexpress_data_warehouse.items import VnexpressDataWarehouseItem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

class BenhdalieuSpider(scrapy.Spider):
    name = "BenhDaLieu"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
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
    ]

    driver = None  # Declare driver outside constructor
    
    def __init__(self, *args, **kwargs):
        super(BenhdalieuSpider, self).__init__(*args, **kwargs)
        self.get_driver()  # Call get_driver to initialize

    def get_driver(self):
        if not self.driver:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse(self, response):
        item = VnexpressDataWarehouseItem()
        # Extract static data using Scrapy selectors
        item['title'] = response.css('h1.title-detail::text').get(default='N/A')
        item['author'] = response.css('div.sidebar-1 > article.fck_detail > p.Normal:last-child > strong::text').get(default='N/A')
        item['date'] = response.css('span.date::text').get(default='N/A')
        item['location'] = response.css('span.location-stamp::text').get(default='N/A')
        item['disease_name'] = response.css('body > section.section.page-detail.top-detail > div > div.sidebar-1 > div.header-content.width_common > ul > li:nth-child(3) > a::text').get(default='N/A')
        item['content'] = ''.join(response.css('article.fck_detail p::text').getall())

        item = self._extract_dynamic_data(response.url, item)
        yield item
        # Extract dynamic data using Selenium in a separate method
        # self._extract_dynamic_data(response.url, item)
        # yield from self._extract_dynamic_data(response.url, item)

        # Follow next page if available
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def _extract_dynamic_data(self, url, item):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 30)

        try:
            comment_count_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="total_comment"]')))
            item['count_comments'] = comment_count_element.text.strip() if comment_count_element else '0'
            print("Comment count:", item['count_comments'])
        except Exception as e:
            item['count_comments'] = '0'
            print("Error getting comment count:", e)

        try:
            likes_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#list_comment > div > div.content-comment > div > div > div.reactions-total > a.number')))
            item['total_like'] = sum(int(element.text.strip()) for element in likes_elements)
            print("Total likes:", item['total_like'])
        except Exception as e:
            item['total_like'] = '0'
            print("Error getting total likes:", e)

        return item  # Return the updated item

    def close_spider(self, spider):
        self.driver.quit()