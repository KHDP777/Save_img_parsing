import requests
from bs4 import BeautifulSoup
import img2pdf
import os

def get_html(url):
    headers = {
        "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent":	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    req = requests.get(url=url, headers=headers)
    with open(f"index.html", "w") as file:
        file.write(req.text)


def list_dir():
    img_list = [f"data/image_{i}.jpeg" for i in range(1, 19 + 1)]
    return img_list

def save_img():
    with open(f"index.html") as file:
        req = file.read()

    soup = BeautifulSoup(req, "lxml")

    all_hrefs = soup.find_all("img", class_="attachment-post-thumbnail wp-post-image")
    count = 0

    for item in all_hrefs:
        count += 1
        # print(item.get("src"))
        url_img = item.get("src")
        req_img = requests.get(url_img)
        response = req_img.content
        with open(f"data/image_{count}.jpeg", "wb") as file:
            file.write(response)
        print(f"Скачан {count} файл...")

url = "https://ekd.me/"

img_list = list_dir()
print(img_list)

with open("result.pdf", "wb") as file:
    file.write(img2pdf.convert(img_list))





