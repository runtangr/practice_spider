import requests
from selenium import webdriver


def selenium_get():
    URL = "https://movie.douban.com/annual/2017#1"
    driver = webdriver.Chrome()
    driver.get(URL)
    # 隐式等待5秒，可以自己调节
    driver.implicitly_wait(5)
    el3 = driver.find_elements_by_xpath('//div[@data-scroll="limited"]/ul/li/a')
    for data in el3:
        print(data.text)


if __name__ == "__main__":
    selenium_get()