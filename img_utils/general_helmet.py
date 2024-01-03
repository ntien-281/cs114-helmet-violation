# Scrapping on Google Images using query "motorcyclist wearing a helmet or no helmet in traffic"

import requests
from bs4 import BeautifulSoup
import os

def get_imgs(url):
    resp = requests.get(url)
    return resp.text

url = "https://www.google.com/search?q=motorcyclist+wearing+a+helmet+or+no+helmet+in+traffic&sca_esv=595369570&tbm=isch&sxsrf=AM9HkKnbsa9NoUJNCqaor3n3wuNibiH_Ig:1704290461153&source=lnms&sa=X&ved=2ahUKEwjCtp_csMGDAxWLs1YBHVfRBj0Q_AUoAXoECAEQAw&biw=1779&bih=869&dpr=1.08"

html_raw = get_imgs(url)
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