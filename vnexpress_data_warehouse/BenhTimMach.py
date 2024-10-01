import scrapy
from vnexpress_data_warehouse.items import VnexpressDataWarehouseItem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

class BenhtimmachSpider(scrapy.Spider):
    name = "BenhTimMach"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/u70-moi-phat-hien-benh-tim-bam-sinh-4797158.html',
        'https://vnexpress.net/meo-an-trung-khong-lam-tang-cholesterol-4795884.html',
        'https://vnexpress.net/tuong-mac-covid-19-hoa-viem-mang-tim-4795826.html',
        'https://vnexpress.net/sot-xuat-huyet-nang-tren-nen-suy-tim-4794475.html',
        'https://vnexpress.net/an-gi-giam-nguy-co-xo-vua-mach-mau-4794238.html',
        'https://vnexpress.net/dau-nguc-gan-hai-thang-boi-tac-mach-mau-nuoi-tim-4794099.html',
        'https://vnexpress.net/nguy-co-dot-quy-do-hep-dong-mach-canh-4793658.html',
        'https://vnexpress.net/nguy-co-dot-quy-do-hep-dong-mach-canh-4793658.html',
        'https://vnexpress.net/thieu-mau-co-tim-do-hep-mach-vanh-4793163.html',
        'https://vnexpress.net/tai-sao-han-che-mon-chien-ran-van-bi-mo-mau-cao-4791764.html',
    ]

    driver = None  # Declare driver outside constructor
    
    def __init__(self, *args, **kwargs):
        super(BenhtimmachSpider, self).__init__(*args, **kwargs)
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