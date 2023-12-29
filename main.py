import os

import requests

BASE_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"

IMG_PATH = "img/bing.jpg"
IMG_PATH_4K = "img/bing_4K.jpg"

_4K = "_UHD.jpg"
_1080P = "_1920x1080.jpg"


def save_img(url, img_path):
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    img = requests.get(url)
    with open(img_path, "wb") as f:
        f.write(img.content)


def main():
    url_resp = requests.get(BASE_URL).json()
    url = url_resp["images"][0]["urlbase"]
    save_img("https://www.bing.com" + url + _1080P, IMG_PATH)
    save_img("https://www.bing.com" + url + _4K, IMG_PATH_4K)


if __name__ == "__main__":
    main()
