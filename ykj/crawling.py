"""
https://m.blog.naver.com/fkdldjs60/221874567247
https://blog.naver.com/fkdldjs60/221911926505
"""

# from google_images_download import google_images_download

# response = google_images_download.googleimagesdownload()

# arguments = {"keywords":"Polar bears, balloons, Beaches", "limit":20, "print_urls":True}
# paths = response.download(arguments)
# print(paths) # 이방법은 지금 크롭 업데이트 이후 되지않습니다.

from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

search_key = "plank+pose"
url = f"https://www.google.com/search?q={quote_plus(search_key)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiCxbSfvtvrAhWrHqYKHSN3C4gQ_AUoAXoECBcQAw&biw=758&bih=714"

# search_key = input("검색할 이미지 : ").replace(" ", "+")
# url = f"https://www.google.com/search?q={quote_plus(search_key)}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiCxbSfvtvrAhWrHqYKHSN3C4gQ_AUoAXoECBcQAw&biw=758&bih=714"

# driver = webdriver.Chrome("C:/Users/kyung/Downloads/chromedriver.exe")
# driver.get(url)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')
# options.add_argument('--hide-scrollbars')
# options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(
    executable_path='C:/Users/kyung/Downloads/chromedriver.exe',
    options=options)
driver.get(url)

html = driver.page_source
# soup = BeautifulSoup(html)
soup = BeautifulSoup(html, "html.parser")
img = soup.select('.rg_i.Q4LuWd')

# cnt = 1
# for i in soup.findAll("img"):
for i in range(400):
    driver.execute_script("window.scrollBy(0, 10000)")
    # cnt += 1

n = 1
imgurl = []

for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

for i in imgurl:
    urlretrieve(
        i, "C:/Users/kyung/Desktop/UPT/Images/" + search_key + str(n) + ".jpg")
    n += 1
    # print(imgurl)
    if (n == 400):
        # if (n == cnt):
        break

driver.close()
