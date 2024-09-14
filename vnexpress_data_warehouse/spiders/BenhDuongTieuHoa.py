import scrapy
import csv

class BenhDuongTieuHoaSpider(scrapy.Spider):
    name = "Benh_Duowng_Tieu_Hoa"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        'https://vnexpress.net/bui-toc-dai-20-cm-lam-tac-ruot-be-gai-4784006.html',
        'https://vnexpress.net/nhung-mon-an-uong-giup-giam-o-nong-4782973.html',
        'https://vnexpress.net/nhung-mon-an-thuc-uong-giup-nhuan-trang-4782543.html',
        'https://vnexpress.net/nhung-loai-nuoc-nen-uong-va-nen-tranh-khi-o-nong-4782418.html',
        'https://vnexpress.net/lam-gi-ngay-sau-khi-non-4782206.html',
        'https://vnexpress.net/suc-khoe/cac-benh/benh-tieu-hoa/benh-duong-tieu-hoa-p2',
        'https://vnexpress.net/an-banh-ngot-buoi-sang-gay-hai-tieu-hoa-the-nao-4786798.html',
        'https://vnexpress.net/6-do-uong-giup-nhuan-trang-4786079.html',
        'https://vnexpress.net/7-loai-tra-giup-giam-day-hoi-4785622.html',
        'https://vnexpress.net/cac-trieu-chung-tieu-hoa-canh-bao-benh-4785101.html',
        'https://vnexpress.net/nhung-mon-an-uong-co-the-gay-hoi-chung-ruot-kich-thich-4784879.html',
        'https://vnexpress.net/suy-kiet-do-viem-loet-dai-trang-boi-nhiem-virus-4784665.html',
        'https://vnexpress.net/nguyen-nhan-dau-bung-sau-an-trai-cay-4784293.html',
        'https://vnexpress.net/dieu-tri-nuot-nghen-do-trao-nguoc-da-day-4778285.html',
        'https://vnexpress.net/9-thuc-pham-can-tranh-an-khi-kho-tieu-4777722.html',
        'https://vnexpress.net/benh-celiac-4776998.html',
        'https://vnexpress.net/trao-nguoc-da-day-thuc-quan-do-thoi-quen-sai-lam-4777225.html',
        'https://vnexpress.net/stress-gay-roi-loan-tieu-hoa-nhu-the-nao-4776864.html',
        'https://vnexpress.net/ai-nen-su-dung-men-tieu-hoa-4776378.html',
        'https://vnexpress.net/8-mon-an-uong-nguoi-dau-da-day-nen-han-che-4776408.html',
        'https://vnexpress.net/loi-ich-khi-uong-nuoc-gung-sau-bua-an-4775647.html',
        'https://vnexpress.net/liet-da-day-4774716.html',
        'https://vnexpress.net/nhung-loai-trai-cay-nen-han-che-an-luc-doi-4773882.html',
        'https://vnexpress.net/an-uong-gi-giup-giam-dau-da-day-nhanh-4773204.html',
        'https://vnexpress.net/hep-hau-mon-bien-chung-nang-sau-mo-tri-4771995.html',
        'https://vnexpress.net/nguyen-nhan-hep-thuc-quan-4770946.html',
        'https://vnexpress.net/dung-thuoc-sai-cach-hai-da-day-4770590.html',
        'https://vnexpress.net/10-cach-giam-roi-loan-tieu-hoa-4770010.html',
        'https://vnexpress.net/polyp-dai-trang-4769281.html'
    ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'location':response.css('span.location-stamp::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('BenhDuongTieuHoa.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'location','url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)