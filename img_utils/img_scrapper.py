import requests
from bs4 import BeautifulSoup
import os

def get_imgs(url):
    resp = requests.get(url)
    return resp.text

vn_top_down_bikers = "https://laodong.vn/photo/bo-anh-goc-chup-nguoi-di-xe-may-tu-tren-cao-dot-nong-cong-dong-mang-644706.ldo"

html_raw = get_imgs(vn_top_down_bikers)
soup = BeautifulSoup(html_raw, 'html.parser')
imgdata = []
for item in soup.findAll('img'):
    try:
        if item["src"]:
            imgdata.append(item["src"])
        elif item["data-src"]:
            imgdata.append(item["data-src"])
    except KeyError as error:
        print(f"Exception {error}")
    finally:
        print("Done")

filename = "helmet_classify_img/picture{}.jpg"
for img in range(len(imgdata)):
    print(f"img {img + 1} / {len(imgdata) + 1}")

    res = requests.get(imgdata[img])
    with open(filename.format(img), "wb") as f:
        f.write(res.content)