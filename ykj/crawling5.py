from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys, os
import urllib, urllib.request
import requests
import random

webDriver = "C:/Users/kyung/Downloads/chromedriver.exe"
folder = "./Images/"
searchItem = "plank+pose"
num = 21
url = "https://www.shutterstock.com/ko/search/" + searchItem + "?page=" + str(
    num)

size = 300

params = {"q": searchItem, "tbm": "isch", "sa": "1", "source": "lnms&tbm=isch"}
url = url + "?" + urllib.parse.urlencode(params)
browser = webdriver.Chrome(webDriver)
time.sleep(0.5)
browser.get(url)
html = browser.page_source
time.sleep(0.5)

# soup_temp = BeautifulSoup(html, 'html.parser')
# img4page = len(soup_temp.select('.z_h_9d80b.z_h_2f2f0'))

elem = browser.find_element_by_tag_name("body")

num_of_pagedowns = 20
while num_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    num_of_pagedowns -= 1

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
img = soup.select('.z_h_9d80b.z_h_2f2f0')

print(len(img))

# next_btn = browser.find_element_by_class_name("z_b_6e283")
# next_btn.click()

fileNum = 2024
srcURL = []

for line in img:
    if str(line).find('src') != -1 and str(line).find('http') < 300:
        print(fileNum, " : ", line['src'])
        srcURL.append(line['src'])
        fileNum += 1
print(fileNum)
# # ### make folder and save picture in that directory

# # saveDir = folder + searchItem

# # try:
# #     if not (os.path.isdir(saveDir)):
# #         os.makedirs(os.path.join(saveDir))
# # except OSError as e:
# #     if e.errno != errno.EEXIST:
# #         print("Failed to create directory!!!!!")
# #         raise

for i, src in zip(range(2024, fileNum), srcURL):
    urllib.request.urlretrieve(src, folder + searchItem + str(i) + ".jpg")
    print(i, "saved")
