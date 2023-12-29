import requests

BASE_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"

IMG_PATH = "img/bing.jpg"


def save_img(url, img_path):
    img = requests.get(url)
    with open(img_path, "wb") as f:
        f.write(img.content)


def main():
    url_resp = requests.get(BASE_URL).json()
    url = url_resp["images"][0]["urlbase"]
    save_img("https://www.bing.com" + url + "_UHD.jpg", IMG_PATH)


if __name__ == "__main__":
    main()
