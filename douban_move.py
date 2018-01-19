import requests
from selenium import webdriver


def selenium_get():
    URL = "https://movie.douban.com/annual/2017#1"
    driver = webdriver.Chrome()
    driver.get(URL)
    el = driver.find_element_by_xpath('//div[@id="app"]/div/div/button')

    el3 = driver.find_elements_by_xpath('//div[@data-scroll="limited"]/ul/li/a')
    for data in el3:
        print(data.text)


if __name__ == "__main__":
    selenium_get()