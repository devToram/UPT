from selenium import webdriver

search_term = 'plankpose'
url = "https://www.google.co.in/search?q="+search_term+"&tbm=isch#imgrc=F-FCwSYY7bWfjM"
browser = webdriver.Chrome("chromedriver.exe")

browser.get(url)

for i in range(500):
    browser.execute_script('window.scrollBy(0,-20000)')

for idx, el in enumerate(browser.find_elements_by_class_name("rg_i")):
    el.screenshot(str(idx)+".png")

browser.close()
