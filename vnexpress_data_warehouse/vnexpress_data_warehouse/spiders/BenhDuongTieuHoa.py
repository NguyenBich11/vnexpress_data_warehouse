
import scrapy
import csv

class BenhDuongTieuHoaSpider(scrapy.Spider):
    name = "Benh_duong_tieu_hoa"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/an-cay-the-nao-khong-hai-da-day-4788119.html',
        'https://vnexpress.net/lam-dung-khang-sinh-gay-hai-duong-ruot-the-nao-4787967.html',
        'https://vnexpress.net/5-thuc-uong-tot-cho-da-day-4787271.html',
        'https://vnexpress.net/an-banh-ngot-buoi-sang-gay-hai-tieu-hoa-the-nao-4786798.html',
        'https://vnexpress.net/6-do-uong-giup-nhuan-trang-4786079.html',
        'https://vnexpress.net/7-loai-tra-giup-giam-day-hoi-4785622.html',
        'https://vnexpress.net/nhung-mon-an-uong-co-the-gay-hoi-chung-ruot-kich-thich-4784879.html',
        'https://vnexpress.net/suy-kiet-do-viem-loet-dai-trang-boi-nhiem-virus-4784665.html',
        'https://vnexpress.net/chuan-bi-gi-khi-noi-soi-dai-trang-4784295.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': '\n'.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('BenhDuongTieuHoa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)