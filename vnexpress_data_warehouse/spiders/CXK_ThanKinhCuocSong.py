import scrapy
import csv


class CxkThankinhcuocsongSpider(scrapy.Spider):
    name = "CXK_ThanKinhCuocSong"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/10-nam-thoat-vi-dia-dem-4787272.html',
                  'https://vnexpress.net/ton-thuong-cot-song-do-nhiem-vi-khuan-an-thit-nguoi-4785175.html#vn_source=Folder-SucKhoe_CacBenh_BenhCoXuongKhop_ThanKinhCotSong&vn_campaign=Stream&vn_medium=Item-2&vn_term=Desktop&vn_thumb=1&vn_aid=1005275',
                  'https://vnexpress.net/di-nhu-robot-do-viem-dinh-cot-song-4781479.html',
                  'https://vnexpress.net/bi-thoat-vi-dia-dem-co-phai-uong-thuoc-suot-doi-khong-4781053.html',
                  'https://vnexpress.net/cac-phuong-phap-dieu-tri-xep-dia-dem-4776119.html',
                  'https://vnexpress.net/12-benh-co-dau-hieu-te-bi-tay-chan-4764764.html',
                  'https://vnexpress.net/dau-hieu-canh-bao-viem-cot-song-dinh-khop-4759683.html',
                  'https://vnexpress.net/6-bai-tap-giam-dau-than-kinh-toa-4758258.html',
                  'https://vnexpress.net/meo-ngu-ngon-cho-nguoi-thoat-vi-dia-dem-4756466.html',
                  'https://vnexpress.net/5-bai-tap-cai-thien-cong-veo-cot-song-4755692.html',
                  'https://vnexpress.net/7-hoat-dong-thuong-ngay-nen-tranh-khi-thoat-vi-dia-dem-4754573.html',
                  'https://vnexpress.net/xep-dot-song-chua-duoc-khong-4754034.html',
                  'https://vnexpress.net/cac-bai-tap-giam-dau-cho-nguoi-thoat-vi-dia-dem-4752752.html',
                  'https://vnexpress.net/thoat-vi-dia-dem-co-chay-bo-duoc-khong-4748728.html',
                  'https://vnexpress.net/tu-the-nam-giam-dau-than-kinh-toa-4741969.html',
                  'https://vnexpress.net/ai-de-bi-gai-cot-song-4740165.html',
                  'https://vnexpress.net/loi-ich-khi-mo-noi-soi-thoat-vi-dia-dem-4724032.html',
                  'https://vnexpress.net/nguyen-nhan-gay-truot-dot-song-4721785.html',
                  'https://vnexpress.net/gu-gap-lung-hai-chi-em-khong-the-nam-ngua-4721369.html',
                  'https://vnexpress.net/dau-dot-song-co-va-that-lung-la-benh-gi-4717325.html',
                  'https://vnexpress.net/thoat-vi-dia-dem-chen-ep-than-kinh-4716821.html',
                  'https://vnexpress.net/dau-hieu-u-cot-song-4716589.html',
                  'https://vnexpress.net/cu-ong-101-tuoi-nga-xep-dot-song-4713736.html',
                  'https://vnexpress.net/tri-hoan-mo-thoat-vi-dia-dem-nguoi-dan-ong-suyt-liet-4713313.html',
                  'https://vnexpress.net/thoi-quen-ngay-tet-gay-dau-lung-4710200.html',
                  'https://vnexpress.net/mo-thoat-vi-dia-dem-cho-nguoi-dai-thao-duong-4709246.html',
                  'https://vnexpress.net/nguy-co-thoat-vi-dia-dem-khi-don-nha-don-tet-4708916.html',
                  'https://vnexpress.net/10-nam-dau-vai-gay-phai-thay-dot-song-nhan-tao-4707665.html',
                  'https://vnexpress.net/cu-ong-94-tuoi-xep-dot-song-do-vac-nang-4702742.html',
                  'https://vnexpress.net/thoat-vi-dia-dem-co-do-thuong-cui-dau-4700957.html',
                  'https://vnexpress.net/cac-dang-cong-veo-cot-song-thuong-gap-4696087.html',
                  'https://vnexpress.net/cot-song-cau-tao-nhu-the-nao-4694465.html',
                  'https://vnexpress.net/dau-hieu-canh-bao-thoat-vi-dia-dem-lung-4690213.html',
                  'https://vnexpress.net/ngu-guc-tren-ban-hai-xuong-khop-4688322.html',
                  'https://vnexpress.net/7-duong-chat-tot-cho-nguoi-benh-thoat-vi-dia-dem-4687454.html',
                  'https://vnexpress.net/benh-cot-song-de-bi-chan-doan-nham-4683981.html',
                  'https://vnexpress.net/khi-nao-can-phau-thuat-hep-ong-song-4683528.html',
                  'https://vnexpress.net/chan-thuong-cot-song-anh-huong-the-nao-den-doi-song-chan-goi-4680852.html',
                  'https://vnexpress.net/ba-cach-giup-dan-van-phong-tranh-dau-cot-song-4680066.html',
                  'https://vnexpress.net/dau-hieu-liet-day-than-kinh-so-7-4677619.html',
                  'https://vnexpress.net/dau-hieu-truot-dot-song-4676716.html',
                  'https://vnexpress.net/dau-hong-khi-ngoi-la-trieu-chung-cua-benh-gi-4676387.html',
                  'https://vnexpress.net/nguyen-nhan-gay-cung-co-4675245.html',
                  'https://vnexpress.net/4-mon-the-thao-tot-cho-nguoi-dau-than-kinh-toa-4674769.html#vn_source=Folder-SucKhoe_CacBenh_BenhCoXuongKhop_ThanKinhCotSong&vn_campaign=Stream&vn_medium=Item-44&vn_term=Desktop&vn_thumb=1&vn_aid=1005275',
                  'https://vnexpress.net/benh-tu-trieu-chung-dau-rat-lung-4667342.html',
                  'https://vnexpress.net/chan-nang-nhu-deo-da-do-day-chang-cot-song-voi-hoa-4664024.html',
                  'https://vnexpress.net/thoi-quen-khi-ngu-khong-tot-cho-cot-song-4662046.html',
                  'https://vnexpress.net/chua-gu-lung-bang-vat-ly-tri-lieu-4660815.html',
                  'https://vnexpress.net/thuong-xuyen-dau-lung-la-benh-gi-4660222.html',
                  'https://vnexpress.net/bien-chung-nguy-hiem-cua-thoat-vi-dia-dem-4657149.html',
                  'https://vnexpress.net/ngoi-cong-lung-hai-xuong-khop-4656733.html',
                  'https://vnexpress.net/cac-benh-dau-co-tay-do-go-may-tinh-nhieu-4654524.html',
                  'https://vnexpress.net/nhung-tu-the-ngoi-hoc-gay-cong-veo-cot-song-4651820.html',
                  'https://vnexpress.net/dau-hieu-ton-thuong-cot-song-4650902.html',
                  'https://vnexpress.net/5-loai-chan-thuong-co-thuong-gap-4647883.html']

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
        with open('CXK_ThanKinhCuocSong.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse),