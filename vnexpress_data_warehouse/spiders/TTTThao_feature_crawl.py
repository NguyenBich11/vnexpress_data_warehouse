import scrapy
from vnexpress_data_warehouse.items import VnexpressDataWarehouseItem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

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
        'https://vnexpress.net/mac-benh-tieu-duong-type-1-hay-type-2-nang-hon-4787888.html',
         'https://vnexpress.net/bien-chung-ban-chan-tieu-duong-ma-khong-biet-4786682.html',
         'https://vnexpress.net/6-mon-chong-viem-cho-nguoi-tieu-duong-4784664.html',
         'https://vnexpress.net/phong-tranh-dai-thao-duong-cho-tre-4783833.html',
         'https://vnexpress.net/dau-hieu-canh-bao-tang-duong-huyet-vao-ban-dem-4782698.html',
         'https://vnexpress.net/dua-cai-chua-anh-huong-den-duong-huyet-the-nao-4780416.html',
         'https://vnexpress.net/cach-phong-benh-tim-mach-do-tieu-duong-4779132.html',
         'https://vnexpress.net/tai-sao-con-tre-van-mac-benh-dai-thao-duong-4778607.html',
         'https://vnexpress.net/an-thit-lon-moi-ngay-co-tang-duong-huyet-4778290.html',
         'https://vnexpress.net/7-yeu-to-loi-song-lam-tang-nguy-co-dai-thao-duong-4778159.html',
         'https://vnexpress.net/bien-chung-dai-thao-duong-type-1-4775488.html',
         'https://vnexpress.net/dau-hieu-tre-mac-benh-tieu-duong-type-1-4775097.html',
         'https://vnexpress.net/vet-thuong-nao-canh-bao-bien-chung-ban-chan-tieu-duong-4773279.html',
         'https://vnexpress.net/mat-thi-luc-bien-chung-am-tham-do-tieu-duong-4772949.html',
         'https://vnexpress.net/loi-ich-cua-ca-rot-voi-nguoi-benh-tieu-duong-4772799.html',
         'https://vnexpress.net/an-gao-lut-co-khoi-benh-dai-thao-duong-4771994.html',
         'https://vnexpress.net/veo-chan-do-bien-chung-tieu-duong-ma-khong-biet-4771860.html',
         'https://vnexpress.net/hai-phoi-trang-xoa-do-nhiem-trung-bien-chung-ban-chan-tieu-duong-4766234.html',
         'https://vnexpress.net/nguoi-tieu-duong-nen-cao-voi-rang-may-lan-mot-nam-4763220.html',
         'https://vnexpress.net/tai-sao-nguoi-tieu-duong-thuong-bi-hu-mong-tay-chan-4760998.html',
         'https://vnexpress.net/nguyen-nhan-da-nguoi-tieu-duong-lao-hoa-nhanh-4760541.html',
         'https://vnexpress.net/benh-vong-mac-tieu-duong-4759992.html',
         'https://vnexpress.net/nhiem-trung-tu-vet-xuoc-nho-nguoi-benh-tieu-duong-phai-cat-bo-chan-4756894.html',
         'https://vnexpress.net/ha-duong-huyet-do-hoi-chung-dumping-4754055.html',
         'https://vnexpress.net/vet-xuoc-nho-tro-nang-do-bien-chung-tieu-duong-4752818.html',
         'https://vnexpress.net/ha-duong-huyet-gay-dot-quy-gia-4749306.html',
         'https://vnexpress.net/bat-ngo-phat-hien-benh-dai-thao-duong-khi-kham-vo-sinh-4738306.html',
         'https://vnexpress.net/nsut-bang-thai-bi-hoai-tu-ban-chan-do-bien-chung-tieu-duong-4737469.html',
         'https://vnexpress.net/hoai-tu-ngon-chan-do-khong-tuan-thu-dieu-tri-tieu-duong-4733422.html',
         'https://vnexpress.net/mac-benh-tieu-duong-sau-5-nam-uong-thuoc-gia-truyen-4730328.html',
         'https://vnexpress.net/lo-la-chua-tieu-duong-nguoi-phu-nu-gap-bien-chung-nang-4728271.html',
         'https://vnexpress.net/tang-duong-huyet-4720398.html',
         'https://vnexpress.net/vet-thuong-nhiem-trung-sau-ngam-vao-nuoc-muoi-4706944.html',
         'https://vnexpress.net/tuong-het-tieu-duong-nguoi-phu-nu-bi-hoai-tu-chan-boi-mun-nhot-4706551.html',
         'https://vnexpress.net/mun-nhot-nhiem-trung-gay-hoai-tu-mong-4705922.html',
         'https://vnexpress.net/nhiem-trung-da-moi-biet-bi-tieu-duong-4704527.html',
         'https://vnexpress.net/khoi-ap-xe-tu-co-lan-den-nguc-nguoi-dan-ong-4699712.html',
         'https://vnexpress.net/vet-thuong-50-nam-kho-lanh-do-tieu-duong-4694776.html',
         'https://vnexpress.net/hai-me-con-bi-bien-chung-tieu-duong-hoai-tu-chan-4688224.html',
         'https://vnexpress.net/thieu-nu-15-tuoi-hon-me-bat-ngo-phat-hien-tieu-duong-4686751.html',
         'https://vnexpress.net/suyt-mat-tinh-hoan-do-bien-chung-tieu-duong-4682982.html',
         'https://vnexpress.net/viem-bao-quy-dau-do-bien-chung-tieu-duong-4670773.html',
         'https://vnexpress.net/nhiem-trung-nang-do-bo-thuoc-tieu-duong-de-bam-huyet-4668235.html',
         'https://vnexpress.net/xem-tieu-duong-nhu-cam-cum-nguoi-dan-ong-bien-chung-nang-4646698.html',
         'https://vnexpress.net/bo-thuoc-chua-tieu-duong-nguoi-phu-nu-tang-duong-huyet-4643333.html',
         'https://vnexpress.net/suyt-chet-sau-hai-thang-uong-thuoc-nam-chua-tieu-duong-4632037.html',
         'https://vnexpress.net/nguy-kich-vi-thuong-xuyen-uong-nuoc-ngot-4608783.html',
         'https://vnexpress.net/nguoi-benh-tieu-duong-suy-da-tang-do-con-trung-chich-4595219.html',
         'https://vnexpress.net/nguy-kich-do-uong-ruou-bo-thuoc-tieu-duong-4590060.html',
         'https://vnexpress.net/virus-tan-cong-vung-kin-nguoi-dai-thao-duong-gay-lo-loet-4584547.html',
         'https://vnexpress.net/buon-non-do-cac-bien-chung-cua-benh-tieu-duong-4584593.html',
        'https://vnexpress.net/kham-suc-khoe-hoc-duong-bac-si-phat-hien-be-gai-bat-thuong-tim-phoi-4688876.html',
        'https://vnexpress.net/vi-khuan-an-thit-nguoi-co-lay-khong-4535888.html',
        'https://vnexpress.net/viem-phoi-do-nam-4520092.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-tre-co-trieu-chung-ho-hap-hau-covid-19-4452703.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-thuoc-dieu-tri-hen-suyen-4437165.html',
        'https://vnexpress.net/benh-bui-phoi-silic-pho-bien-o-nguoi-tren-40-4436530.html',
        'https://vnexpress.net/benh-sarcoidosis-dau-hieu-nguyen-nhan-va-phuong-phap-dieu-tri-4436531.html',
        'https://vnexpress.net/benh-phoi-hiem-gap-khien-be-gai-9-nam-thieu-mau-3730384.html',
        'https://vnexpress.net/kho-tho-do-vo-ken-khi-phoi-4769681.html',
        'https://vnexpress.net/ba-phuong-phap-dieu-tri-suy-tuyen-yen-4787721.html',
        'https://vnexpress.net/nhan-giap-xam-lan-sun-khi-quan-nguoi-dan-ong-4787623.html',
        'https://vnexpress.net/dau-hieu-tre-thieu-hormone-tang-truong-4782224.html',
        'https://vnexpress.net/dung-uong-sua-bo-co-ngan-day-thi-som-4777030.html',
        'https://vnexpress.net/mo-tham-my-nhan-tuyen-giap-4776624.html',
        'https://vnexpress.net/ha-canxi-mau-4771495.html',
        'https://vnexpress.net/tiem-hormone-kim-ham-day-thi-som-cho-be-gai-7-tuoi-4765899.html',
        'https://vnexpress.net/dai-thao-nhat-trung-uong-4764597.html',
        'https://vnexpress.net/suy-tuyen-thuong-than-la-benh-gi-4764233.html',
        'https://vnexpress.net/dai-thao-nhat-do-than-4752030.html',
        'https://vnexpress.net/tuong-benh-duong-ruot-hoa-suy-giap-4750597.html',
        'https://vnexpress.net/ha-kali-mau-4749619.html',
        'https://vnexpress.net/7-mon-an-bo-sung-noi-tiet-to-nu-4749226.html',
        'https://vnexpress.net/tang-huyet-ap-keo-dai-moi-phat-hien-do-u-tuyen-thuong-than-4747608.html',
        'https://vnexpress.net/tu-choi-mo-u-tuy-thuong-than-nguoi-phu-nu-nhieu-lan-tang-huyet-ap-4745304.html',
        'https://vnexpress.net/10-tu-the-yoga-giup-can-bang-noi-tiet-to-4743714.html',
        'https://vnexpress.net/loi-ich-cua-yoga-trong-dieu-hoa-noi-tiet-to-4743530.html',
        'https://vnexpress.net/meo-can-bang-noi-tiet-to-nu-4739829.html',
        'https://vnexpress.net/thieu-nu-17-tuoi-thieu-hut-90-hormone-noi-tiet-do-u-tuyen-yen-4739593.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-hoi-chung-cushing-4738977.html',
        'https://vnexpress.net/4-cach-giup-giam-can-o-tuoi-day-thi-4737260.html',
        'https://vnexpress.net/dai-thao-nhat-o-tre-em-co-nguy-hiem-4733833.html',
        'https://vnexpress.net/6-do-uong-giup-phai-dep-tang-cuong-noi-tiet-to-4731613.html',
        'https://vnexpress.net/8-meo-tang-noi-tiet-to-cho-nam-gioi-4724086.html',
        'https://vnexpress.net/lam-dung-thuoc-corticoid-giam-dau-khien-suy-tuyen-thuong-than-4712412.html',
        'https://vnexpress.net/suy-tuyen-thuong-than-dieu-tri-tai-nha-can-luu-y-gi-4693957.html',
        'https://vnexpress.net/moi-nguy-do-lam-dung-thuoc-giam-dau-chua-corticoid-4680631.html',
        'https://vnexpress.net/thua-canxi-trong-mau-co-nguy-hiem-4678388.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-tut-canxi-4677473.html',
        'https://vnexpress.net/tuong-phat-tuong-sau-ket-hon-hoa-u-tuyen-thuong-than-4675301.html',
        'https://vnexpress.net/sot-xuat-huyet-chong-benh-suy-tuyen-yen-4673655.html',
        'https://vnexpress.net/het-dau-dau-sau-mo-u-thuong-than-4670147.html',
        'https://vnexpress.net/bien-chung-sau-ba-thang-uong-thuc-pham-chuc-nang-chua-corticoid-4667402.html',
        'https://vnexpress.net/tai-sao-tre-mac-hoi-chung-cushing-4663890.html',
        'https://vnexpress.net/estrogen-tac-dong-the-nao-voi-sinh-ly-phai-dep-4660709.html',
        'https://vnexpress.net/15-thuc-pham-bo-sung-noi-tiet-to-cho-phu-nu-4655321.html',
        'https://vnexpress.net/dot-quy-tuyen-yen-la-benh-gi-4648556.html',
        'https://vnexpress.net/dai-thao-nhat-la-benh-gi-4639084.html',
        'https://vnexpress.net/an-nhieu-duong-tinh-bot-co-anh-huong-sinh-ly-nam-4636974.html',
        'https://vnexpress.net/16-dau-hieu-can-bo-sung-noi-tiet-to-nu-4636172.html',
        'https://vnexpress.net/5-cach-bao-ve-da-khoi-mun-noi-tiet-4629030.html',
        'https://vnexpress.net/9-cach-can-bang-noi-tiet-to-sau-sinh-4626722.html',
        'https://vnexpress.net/roi-loan-noi-tiet-sau-sinh-co-bat-thuong-4625512.html',
        'https://vnexpress.net/dau-hieu-nao-canh-bao-suy-giam-noi-tiet-to-4624592.html',
        'https://vnexpress.net/7-xet-nghiem-noi-tiet-to-nu-thuong-gap-4623694.html',
        'https://vnexpress.net/8-ly-do-gay-suy-giam-noi-tiet-to-nu-4614428.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-benh-tuyen-giap-4613003.html',
        'https://vnexpress.net/10-cach-can-bang-noi-tiet-to-cho-phu-nu-4610304.html',
        'https://vnexpress.net/cham-soc-da-mun-do-thay-doi-noi-tiet-the-nao-4607042.html',
        'https://vnexpress.net/lam-the-nao-nhan-biet-mat-can-bang-noi-tiet-to-nu-4606055.html',
        'https://vnexpress.net/10-benh-lien-quan-den-roi-loan-noi-tiet-4600946.html',
        'https://vnexpress.net/cach-dieu-tri-nam-da-do-thay-doi-noi-tiet-to-4596093.html',
        'https://vnexpress.net/phan-biet-nam-nang-va-nam-da-do-thay-doi-noi-tiet-4578924.html',
        'https://vnexpress.net/u-tuyen-tuy-gay-ha-duong-huyet-hon-me-4578304.html',
        'https://vnexpress.net/4-nguyen-nhan-thuong-gap-lam-thay-doi-noi-tiet-gay-nam-4574708.html',
        'https://vnexpress.net/roi-loan-noi-tiet-anh-huong-den-viem-da-co-dia-4490189.html',
        'https://vnexpress.net/hoi-chung-kallmann-gay-mat-khuu-giac-can-tro-day-thi-4487829.html',
        'https://vnexpress.net/noi-tiet-to-nu-anh-huong-the-nao-den-suc-khoe-4480771.html',
        'https://vnexpress.net/cac-benh-roi-loan-noi-tiet-thuong-gap-4479127.html',
        'https://vnexpress.net/dau-hieu-nhan-biet-phu-nu-beo-bung-do-roi-loan-noi-tiet-4473844.html',
        'https://vnexpress.net/4-lam-tuong-ve-bo-sung-noi-tiet-to-4454353.html',
        'https://vnexpress.net/5-cach-can-bang-noi-tiet-to-de-tang-kha-nang-thu-thai-4438878.html',
        'https://vnexpress.net/nguyen-nhan-gay-roi-loan-noi-tiet-to-kho-thu-thai-4437365.html',
        'https://vnexpress.net/lieu-phap-noi-tiet-chua-khoi-ung-thu-vu-ma-khong-can-hoa-tri-3786452.html',
        'https://vnexpress.net/6-bien-chung-ung-thu-phoi-4683906.html',
        'https://vnexpress.net/tai-sao-phu-nu-co-nguy-co-mac-ung-thu-phoi-cao-hon-nam-gioi-4462136.html',
        'https://vnexpress.net/cach-nhan-biet-cac-truong-hop-khan-cap-ve-ung-thu-phoi-4453067.html',
        'https://vnexpress.net/9-dau-hieu-canh-bao-benh-phoi-can-som-tam-soat-4449693.html',
        'https://vnexpress.net/6-dau-hieu-canh-bao-som-benh-ung-thu-phoi-4449179.html',
        'https://vnexpress.net/phat-hien-som-benh-ho-hap-nho-noi-soi-phe-quan-ong-mem-4444676.html',
        'https://vnexpress.net/u-phoi-lanh-tinh-phat-hien-som-se-giam-nguy-co-bien-chung-4436932.html',
        'https://vnexpress.net/hen-o-tre-nho-kho-chan-doan-4391014.html',
        'https://vnexpress.net/phan-biet-trieu-chung-covid-19-va-benh-phoi-tac-nghen-man-tinh-4381646.html',
        'https://vnexpress.net/nhung-dieu-can-biet-ve-noi-soi-phe-quan-ong-mem-4351887.html',
        'https://vnexpress.net/phat-hien-cham-soc-nguoi-benh-phoi-tac-nghen-man-tinh-trong-dich-covid-19-4355556.html',
        'https://vnexpress.net/5-thuc-pham-giup-giam-ho-4787558.html',
        'https://vnexpress.net/che-do-dinh-duong-cho-tre-viem-duong-ho-hap-4787582.html',
        'https://vnexpress.net/4-luu-y-de-tho-dung-cach-khi-chay-bo-4787037.html',
        'https://vnexpress.net/thu-pham-gay-benh-ho-hap-o-nguoi-cao-tuoi-khi-giao-mua-4786497.html',
        'https://vnexpress.net/5-cach-ngan-mui-hoi-tho-buoi-sang-4786394.html',
        'https://vnexpress.net/phoi-ton-thuong-hinh-choi-cay-do-lao-4786367.html',
        'https://vnexpress.net/nhung-mon-an-uong-nen-tranh-khi-ho-4786135.html',
        'https://vnexpress.net/nguyen-nhan-it-ngo-gay-kho-tho-4785689.html',
        'https://vnexpress.net/7-loai-thao-moc-giup-giam-mui-hoi-tho-4785295.html',
        'https://vnexpress.net/lam-the-nao-giam-ho-nhanh-khong-dung-thuoc-4785261.html',
        'https://vnexpress.net/cam-cum-va-cam-lanh-khac-nhau-the-nao-4784903.html',
        'https://vnexpress.net/lam-the-nao-khu-mui-bia-ruou-gay-hoi-mieng-4784787.html',
        'https://vnexpress.net/duong-lay-nhiem-vi-khuan-an-thit-nguoi-4784108.html',
        'https://vnexpress.net/an-uong-the-nao-de-hoi-tho-thom-mat-4783505.html',
        'https://vnexpress.net/ly-do-phu-nu-man-kinh-thuong-ngay-ngu-4783577.html',
        'https://vnexpress.net/ban-biet-gi-ve-tho-5-ngon-tay-4783181.html',
        'https://vnexpress.net/dung-la-trau-the-nao-giam-mui-hoi-mieng-4782713.html',
        'https://vnexpress.net/lam-the-nao-phong-benh-ho-hap-cho-tre-mua-tuu-truong-4782411.html',
        'https://vnexpress.net/nhung-loai-cu-qua-nen-an-thuong-xuyen-de-tang-mien-dich-4782034.html',
        'https://vnexpress.net/4-thoi-quen-an-uong-khien-hoi-tho-co-mui-4781725.html',
        'https://vnexpress.net/ngu-ngay-gay-hai-the-nao-4781321.html',
        'https://vnexpress.net/gia-vi-nao-ho-tro-thong-thoang-duong-tho-4781039.html',
        'https://vnexpress.net/nguyen-nhan-khien-phoi-lao-hoa-4780476.html',
        'https://vnexpress.net/bai-tap-nao-giup-giam-ngu-ngay-4780112.html',
        'https://vnexpress.net/thoi-quen-truoc-khi-ngu-tot-cho-ho-hap-4779874.html',
        'https://vnexpress.net/5-lam-tuong-ve-ngung-tho-khi-ngu-4779493.html',
        'https://vnexpress.net/thieu-ngu-tang-nguy-co-mac-benh-ho-hap-4779193.html',
        'https://vnexpress.net/bi-quyet-chay-bo-khong-kho-tho-4779096.html',
        'https://vnexpress.net/thoi-quen-nao-khien-phoi-dan-suy-kiet-4778737.html',
        'https://vnexpress.net/ve-sinh-phong-ngu-dung-cach-the-nao-4777867.html',
        'https://vnexpress.net/tran-dich-mang-phoi-4777406.html',
        'https://vnexpress.net/nghien-thuoc-la-bia-ruou-tang-nguy-co-ngung-tho-khi-ngu-4776181.html',
        'https://vnexpress.net/benh-lao-4775730.html',
        'https://vnexpress.net/dau-hieu-thieu-oxy-khi-ngu-4775720.html',
        'https://vnexpress.net/thuyen-tac-phoi-4773702.html',
        'https://vnexpress.net/10-cach-tang-kha-nang-mien-dich-cua-co-the-4773738.html',
        'https://vnexpress.net/cach-don-gian-thanh-loc-khong-khi-trong-nha-4773281.html',
        'https://vnexpress.net/an-gi-de-tang-mien-dich-it-om-vat-4773000.html',
        'https://vnexpress.net/khoi-bep-an-co-the-gay-benh-phoi-4772286.html',
        'https://vnexpress.net/an-nhieu-kem-uong-nuoc-da-de-benh-ho-hap-4771666.html',
        'https://vnexpress.net/trieu-chung-benh-bach-hau-khac-cam-covid-19-the-nao-4769080.html',
        'https://vnexpress.net/trieu-chung-benh-bach-hau-khac-cam-covid-19-the-nao-4769080.html',
        'https://vnexpress.net/5-thuc-pham-giup-giam-ngu-ngay-4769152.html',
        'https://vnexpress.net/cac-mon-an-co-the-hai-phoi-4768356.html',
        'https://vnexpress.net/6-mon-an-uong-bo-phoi-4766949.html',
        'https://vnexpress.net/nguoi-benh-hen-suyen-co-nen-uong-ca-phe-muoi-4766842.html',
        'https://vnexpress.net/nhung-dieu-it-biet-ve-phoi-4761992.html',
        'https://vnexpress.net/viem-phoi-do-nhiem-nam-4761139.html',
        'https://vnexpress.net/dau-hieu-nao-canh-bao-can-kham-phoi-4758672.html',
        'https://vnexpress.net/mang-phoi-san-sui-nhu-san-ho-do-ung-thu-di-can-4758010.html',
        'https://vnexpress.net/cham-soc-tre-so-sinh-viem-phoi-4757725.html',
        'https://vnexpress.net/tai-sao-phoi-suy-yeu-4755651.html',
        'https://vnexpress.net/tai-sao-viem-hong-de-bien-thanh-viem-phoi-4751230.html',
        'https://vnexpress.net/ngung-tho-khi-ngu-4750578.html',
        'https://vnexpress.net/lay-cum-trong-gia-dinh-ba-nguoi-nhap-vien-4750166.html',
        'https://vnexpress.net/hut-thuoc-la-hai-phoi-the-nao-4743290.html',
        'https://vnexpress.net/khong-hut-thuoc-nhieu-nguoi-van-mac-ung-thu-phoi-4737842.html',
        'https://vnexpress.net/nhieu-nguoi-nhap-vien-vi-cum-mua-bien-chung-viem-phoi-4737858.html',
        'https://vnexpress.net/kiem-tra-de-biet-ban-co-nguy-co-ung-thu-phoi-khong-4735062.html',
        'https://vnexpress.net/sot-ret-keo-dai-phat-hien-lao-mang-phoi-4732738.html',
        'https://vnexpress.net/cu-ong-nam-mot-cho-lau-ngay-bi-viem-phoi-loet-da-nang-4730575.html',
        'https://vnexpress.net/bien-chung-nguy-hiem-cua-cum-4726260.html',
        'https://vnexpress.net/ai-co-nguy-co-mac-benh-bui-phoi-4725881.html',
        'https://vnexpress.net/mac-thuy-dau-bien-chung-thanh-viem-phoi-4725419.html',
        'https://vnexpress.net/ho-ra-mau-o-at-do-gian-dong-mach-phe-quan-4724513.html',
        'https://vnexpress.net/mui-nen-thom-co-the-gay-benh-4719117.html',
        'https://vnexpress.net/tang-ap-phoi-tro-nang-khien-nguoi-phu-nu-ngat-xiu-4718196.html',
        'https://vnexpress.net/ap-xe-phoi-do-hoc-xuong-4715356.html',
        'https://vnexpress.net/dau-hieu-nhiem-virus-hop-bao-ho-hap-4714592.html',
        'https://vnexpress.net/viem-trang-phoi-sau-chuyen-leo-nui-4708745.html'
    ]

    def __init__(self, *args, **kwargs):
        super(BenhtimmachSpider, self).__init__(*args, **kwargs)
        # Khởi tạo Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        # Dùng Selenium để mở trang
        self.driver.get(response.url)
        # Đợi trang tải hoàn toàn (tối đa 10 giây)
        self.driver.implicitly_wait(10)

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
            with open('TTTThao_feature_crawl.csv', 'r', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open('TTTThao_feature_crawl.csv', 'a', newline='', encoding='utf-8') as csvfile:
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
