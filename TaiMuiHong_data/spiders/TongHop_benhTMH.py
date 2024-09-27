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

class TongHop_benhTMH(scrapy.Spider):
    name = "TongHop_benhTMH"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/u-tai-do-thung-mang-nhi-4786434.html',
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
                  'https://vnexpress.net/4-benh-mui-xoang-de-nham-lan-trieu-chung-4782494.html',
                  'https://vnexpress.net/lech-vach-ngan-mui-co-tai-phat-sau-phau-thuat-4780752.html',
                  'https://vnexpress.net/mat-khuu-giac-co-the-chua-khoi-khong-4779811.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/9-cach-don-gian-giup-giam-so-mui-4774663.html',
                  'https://vnexpress.net/nhung-hieu-lam-thuong-gap-ve-viem-xoang-4767610.html',
                  'https://vnexpress.net/cuon-mui-gian-no-do-lam-dung-thuoc-nho-mui-4767601.html',
                  'https://vnexpress.net/tre-tai-phat-viem-mui-xoang-do-di-boi-4765900.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/viem-mui-xoang-di-ung-co-can-xet-nghiem-tim-nguyen-nhan-4763199.html',
                  'https://vnexpress.net/lam-dung-thuoc-nho-mui-gay-bien-chung-4756694.html',
                  'https://vnexpress.net/tuong-u-tai-hoa-phi-dai-cuon-mui-4753783.html',
                  'https://vnexpress.net/qua-phat-cuon-mui-4753159.html'
                  'https://vnexpress.net/nen-va-khong-nen-lam-gi-khi-cam-lanh-4722959.html',
                  'https://vnexpress.net/nhieu-nguoi-chay-mau-cam-do-nang-nong-4718663.html',
                  'https://vnexpress.net/nhieu-nguoi-viem-tai-mui-hong-sau-tet-4716515.html',
                  'https://vnexpress.net/viem-mui-di-ung-mua-xuan-4711777.html',
                  'https://vnexpress.net/khoi-huong-anh-huong-den-nguoi-viem-mui-xoang-the-nao-4709688.html',
                  'https://vnexpress.net/co-nen-phau-thuat-chua-phi-dai-cuon-mui-4707483.html',
                  'https://vnexpress.net/trieu-chung-viem-mui-xoang-4707387.html',
                  'https://vnexpress.net/he-qua-kho-luong-khi-nhin-hat-hoi-4705705.html',
                  'https://vnexpress.net/8-cach-giup-giam-di-ung-4697348.html',
                  'https://vnexpress.net/tai-sao-ban-chay-nuoc-mui-4697355.html',
                  'https://vnexpress.net/dau-hieu-nhan-biet-ung-thu-mui-4694235.html',
                  'https://vnexpress.net/cach-ngan-ngua-viem-mui-di-ung-4692565.html',
                  'https://vnexpress.net/viem-xoang-chay-mau-mui-nguy-hiem-khong-4692049.html',
                  'https://vnexpress.net/dau-hieu-nhan-biet-ung-thu-xoang-4691189.html',
                  'https://vnexpress.net/cach-tranh-di-ung-voi-cay-thong-noel-4690202.html',
                  'https://vnexpress.net/su-that-thu-vi-ve-mui-nguoi-4688828.html',
                  'https://vnexpress.net/nguyen-nhan-khuu-giac-cua-ban-thay-doi-4688253.html',
                  'https://vnexpress.net/cach-don-gian-phong-viem-xoang-4687834.html',
                  'https://vnexpress.net/mo-xoang-bao-lau-hoi-phuc-4683467.html',
                  'https://vnexpress.net/an-gi-khi-chay-mau-cam-4680718.html',
                  'https://vnexpress.net/dau-dau-do-viem-xoang-dieu-tri-the-nao-4680241.html',
                  'https://vnexpress.net/trieu-chung-nhiem-trung-xoang-lan-len-nao-4676904.html',
                  'https://vnexpress.net/hep-eo-hong-nguoi-dan-ong-thuong-ngat-tho-khi-ngu-4675560.html',
                  'https://vnexpress.net/tai-sao-mui-thuong-nghet-vao-buoi-sang-4674149.html',
                  'https://vnexpress.net/nam-lap-day-cac-xoang-cua-nguoi-dan-ong-4671435.html',
                  'https://vnexpress.net/polyp-mui-co-tu-khoi-khong-4670862.html',
                  'https://vnexpress.net/7-thuc-pham-tot-cho-nguoi-benh-viem-xoang-4670701.html',
                  'https://vnexpress.net/nguyen-nhan-kho-mui-4670163.html',
                  'https://vnexpress.net/5-loai-tra-giup-giam-nghet-mui-4667503.html',
                  'https://vnexpress.net/dau-hieu-nhiem-ky-sinh-trung-tai-mui-hong-4559846.html',
                  'https://vnexpress.net/viem-xoang-co-lay-khi-thoi-tiet-lanh-4550783.html',
                  'https://vnexpress.net/8-trieu-chung-canh-bao-mac-nhiem-trung-xoang-4548151.html',
                  'https://vnexpress.net/viem-xoang-do-nam-4545696.html',
                  'https://vnexpress.net/cach-xu-tri-viem-xoang-tai-phat-mua-lanh-4544208.html',
                  'https://vnexpress.net/chay-mau-cam-do-di-ung-4542679.html',
                  'https://vnexpress.net/cac-bai-tap-tho-tot-cho-mui-4542459.html',
                  'https://vnexpress.net/xu-tri-nghet-mui-cho-tre-dung-cach-4541909.html',
                  'https://vnexpress.net/5-sai-lam-can-tranh-khi-tu-dieu-tri-nhiem-trung-xoang-4539447.html',
                  'https://vnexpress.net/4-loai-thuc-pham-nguoi-benh-viem-xoang-nen-han-che-4538012.html',
                  'https://vnexpress.net/cach-xu-ly-mun-moc-o-mui-4537368.html',
                  'https://vnexpress.net/cach-xu-ly-mun-moc-o-mui-4537368.html',
                  'https://vnexpress.net/dau-khi-nhai-canh-bao-sau-rang-ung-thu-mieng-4537269.html',
                  'https://vnexpress.net/cach-cai-thien-di-ung-mui-4534791.html',
                  'https://vnexpress.net/hut-thuoc-la-gay-hai-cho-mui-xoang-4534212.html',
                  'https://vnexpress.net/co-nen-dung-nuoc-muoi-rua-mui-cho-tre-keo-dai-4533758.html',
                  'https://vnexpress.net/viem-mui-khi-mang-thai-4532926.html',
                  'https://vnexpress.net/8-nguyen-nhan-gay-ngua-mui-4530918.html',
                  'https://vnexpress.net/nguyen-nhan-gay-chay-dich-mui-sau-4513778.html',
                  'https://vnexpress.net/8-meo-giup-de-ngu-khi-bi-nghet-mui-4512537.html',
                  'https://vnexpress.net/5-cach-giup-giam-so-mui-4511128.html',
                  'https://vnexpress.net/8-meo-giup-cai-thien-ngua-mui-4506675.html',
                  'https://vnexpress.net/4-cach-giam-trieu-chung-viem-xoang-tai-nha-4506258.html',
                  'https://vnexpress.net/chay-mau-cam-do-cang-thang-4506556.html',
                  'https://vnexpress.net/cach-giam-nghet-mui-don-gian-tai-nha-4501045.html',
                  'https://vnexpress.net/cach-xong-hoi-bang-thao-moc-giup-thong-mui-4496788.html',
                  'https://vnexpress.net/noi-hach-o-co-co-phai-ung-thu-4780340.html',
                  'https://vnexpress.net/ai-co-nguy-co-ung-thu-vom-hong-4764545.html',
                  'https://vnexpress.net/khi-nao-nen-tam-soat-ung-thu-tai-mui-hong-4756286.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-4754883.html',
                  'https://vnexpress.net/viem-mui-hong-thuong-xuyen-do-va-khong-tieu-bien-4777385.html',
                  'https://vnexpress.net/ung-thu-tai-mui-hong-4728889.html',
                  'https://vnexpress.net/ung-thu-ham-4726086.html',
                  'https://vnexpress.net/ung-thu-xoang-4724895.html',
                  'https://vnexpress.net/ung-thu-amidan-4717052.html',
                  'https://vnexpress.net/co-can-phau-thuat-soi-tuyen-nuoc-bot-duoi-luoi-4712326.html',
                  'https://vnexpress.net/ly-giai-ve-phan-xa-ngap-4682425.html',
                  'https://vnexpress.net/5-mon-an-phong-ung-thu-dau-co-4664707.html',
                  'https://vnexpress.net/cach-dao-thai-soi-tuyen-nuoc-bot-4639958.html'
                  'https://vnexpress.net/bien-dang-mat-do-soi-duoi-ham-4638478.html',
                  'https://vnexpress.net/mu-mat-trai-sau-tai-nan-chan-thuong-ham-mat-4601708.html',
                  'https://vnexpress.net/chua-tram-cam-mot-nam-moi-biet-roi-loan-tien-dinh-4541714.html',
                  'https://vnexpress.net/nhai-nuot-kho-di-kham-phat-hien-u-xuong-ham-4527576.html',
                  'https://vnexpress.net/cac-loai-thuc-uong-giup-giam-nhiet-mieng-4489665.html',
                  'https://vnexpress.net/7-dau-hieu-canh-bao-ung-thu-thuc-quan-4487585.html',
                  'https://vnexpress.net/dau-hieu-canh-bao-ung-thu-vom-hong-4481963.html',
                  'https://vnexpress.net/hon-co-the-lam-lay-lan-nhung-benh-gi-4455894.html',
                  'https://vnexpress.net/oral-sex-co-the-lay-truyen-virus-gay-ung-thu-vom-hong-4455396.html',
                  'https://vnexpress.net/9-thuc-pham-giau-iot-phong-ngua-buou-co-4455057.html',
                  'https://vnexpress.net/noi-hach-o-co-khi-nao-nguy-hiem-4446139.html',
                  'https://vnexpress.net/5-loai-ung-thu-vung-dau-co-thuong-gap-4446226.html',
                  'https://vnexpress.net/dieu-tri-u-nang-keo-tuyen-giap-4400886.html',
                  'https://vnexpress.net/u-tuyen-giap-khi-nao-phat-trien-thanh-ung-thu-4398938.html',
                  'https://vnexpress.net/dieu-tri-roi-loan-giong-noi-tuoi-day-thi-the-nao-4781180.html',
                  'https://vnexpress.net/ve-sinh-rang-mieng-ky-sao-hoi-tho-van-co-mui-4778484.html',
                  'https://vnexpress.net/nam-noi-giong-nu-chua-nhu-the-nao-4778128.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/viem-mui-hong-thuong-xuyen-do-va-khong-tieu-bien-4777385.html',
                  'https://vnexpress.net/tho-khi-dung-tai-nha-duoc-khong-4775466.html',
                  'https://vnexpress.net/vet-loet-do-nhiet-mieng-co-khac-ung-thu-luoi-4775220.html',
                  'https://vnexpress.net/cac-mon-nen-an-va-tranh-khi-nhiet-mieng-4774741.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/nhung-benh-thuong-gay-dau-hong-4771957.html',
                  'https://vnexpress.net/hoi-chung-ngung-tho-khi-ngu-4770417.html',
                  'https://vnexpress.net/co-nen-dung-nuoc-muoi-sinh-ly-suc-hong-rua-mui-moi-ngay-4768947.html',
                  'https://vnexpress.net/co-can-cat-thang-luoi-cho-tre-4768561.html'
                  'https://vnexpress.net/manh-xuong-ca-dam-vao-luoi-nguoi-dan-ong-4766366.html',
                  'https://vnexpress.net/meo-phong-dau-hong-ngay-nang-4765450.html',
                  'https://vnexpress.net/nguoi-lon-tuoi-co-phau-thuat-amidan-duoc-khong-4763918.html',
                  'https://vnexpress.net/ngu-ngay-co-phai-la-benh-4763644.html',
                  'https://vnexpress.net/cat-amidan-bao-lau-co-the-an-uong-binh-thuong-4761724.html',
                  'https://vnexpress.net/hoc-di-vat-mui-hong-tai-nan-thuong-gap-o-tre-nho-4760859.html',
                  'https://vnexpress.net/viem-amidan-benh-de-tai-phat-mua-he-4758338.html',
                  'https://vnexpress.net/suc-khoe/cac-benh/benh-tai-mui-hong/hong-thanh-quan-p4',
                  'https://vnexpress.net/mat-giong-do-polyp-day-thanh-quan-4751454.html',
                  'https://vnexpress.net/hoi-chung-bong-rat-mieng-4727520.html',
                  'https://vnexpress.net/5-o-chua-nhieu-mam-benh-cam-lanh-4723569.html',
                  'https://vnexpress.net/viem-amidan-hoc-mu-4719193.html',
                  'https://vnexpress.net/9-mon-an-uong-tot-cho-nguoi-dau-hong-4718648.html',
                  'https://vnexpress.net/mau-sac-o-luoi-canh-bao-benh-gi-4718257.html',
                  'https://vnexpress.net/9-benh-ve-luoi-4715719.html',
                  'https://vnexpress.net/cat-amidan-bao-lau-co-the-uong-ruou-bia-4709682.html',
                  'https://vnexpress.net/cach-nao-phong-nhiet-mieng-ngay-tet-4710048.html',
                  'https://vnexpress.net/cach-giam-kho-rat-hong-sau-khi-uong-ruou-bia-4709946.html',
                  'https://vnexpress.net/nguyen-nhan-gay-benh-luoi-trang-4708565.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-co-thanh-ung-thu-4706609.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-duoi-ham-4705269.html',
                  'https://vnexpress.net/dau-hieu-o-luoi-canh-bao-co-the-thieu-vitamin-d-4704352.html',
                  'https://vnexpress.net/tai-sao-ngay-to-hon-sau-khi-uong-ruou-4704398.html',
                  'https://vnexpress.net/meo-giam-kho-mieng-4702038.html',
                  'https://vnexpress.net/tai-sao-chay-nuoc-dai-khi-ngu-4700805.html',
                  'https://vnexpress.net/tai-sao-chay-nuoc-dai-khi-ngu-4700805.html',
                  'https://vnexpress.net/khan-tieng-canh-bao-benh-gi-4700518.html',
                  'https://vnexpress.net/sai-lam-khi-dung-nuoc-suc-mieng-4699734.html',
                  'https://vnexpress.net/nguyen-nhan-hoi-tho-co-mui-khong-do-thuc-pham-4699028.html',
                  'https://vnexpress.net/9-nguyen-nhan-gay-ngu-ngay-4698222.html',
                  'https://vnexpress.net/tai-tao-khi-quan-cho-nguoi-bi-bien-chung-sau-dot-quy-4696683.html',
                  'https://vnexpress.net/ho-khien-co-the-dot-chay-bao-nhieu-nang-luong-4695941.html',
                  'https://vnexpress.net/6-cach-lam-diu-co-hong-sau-khi-non-4694508.html',
                  'https://vnexpress.net/6-mon-an-uong-lam-tang-dom-4694925.html',
                  'https://vnexpress.net/6-mon-an-uong-tieu-dom-4693471.html',
                  'https://vnexpress.net/7-cach-loai-bo-dom-o-hong-4692983.html',
                  'https://vnexpress.net/6-mon-an-tang-mien-dich-phong-cam-cum-4689193.html',
                  'https://vnexpress.net/cach-giam-dau-hong-co-dom-mua-lanh-4687824.html',
                  'https://vnexpress.net/cam-giac-on-lanh-do-dau-4687552.html',
                  'https://vnexpress.net/phau-thuat-3-trong-1-chua-ngu-ngay-4684271.html',
                  'https://vnexpress.net/meo-bao-ve-giong-noi-trong-treo-4683942.html',
                  'https://vnexpress.net/mo-tuyen-giap-lac-cho-khien-nguoi-phu-nu-kho-nuot-4683315.html',
                  'https://vnexpress.net/tai-sao-kho-mieng-4680250.html',
                  'https://vnexpress.net/kieng-gi-khi-viem-hong-de-nhanh-khoi-benh-4678212.html',
                  'https://vnexpress.net/nguyen-nhan-gay-chua-mieng-4675373.html',
                  'https://vnexpress.net/cong-dung-giam-ho-cua-tinh-dau-4672944.html',
                  'https://vnexpress.net/viem-amidan-man-tinh-co-gay-ung-thu-4671019.html',
                  'https://vnexpress.net/ngu-ngay-nhu-sam-bat-ngo-phat-hien-viem-amidan-4668372.html',
                  'https://vnexpress.net/6-cach-giam-ngua-hong-4650860.html',
                  
    ]

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
            with open('TongHopTMH.csv', 'r', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open('TongHopTMH.csv', 'a', newline='', encoding='utf-8') as csvfile:
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