from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver/chromedriver.exe")
kevcase_899 = "https://smartstore.naver.com/hyotrade/products/4809552659"
kevcase_599 = "https://smartstore.naver.com/hyotrade/products/5006125821"
acat_x1 = "https://smartstore.naver.com/hyotrade/products/5092067009"
SGPC_K77 = "https://smartstore.naver.com/hyotrade/products/4823734246"
list = [kevcase_599, kevcase_899, acat_x1, SGPC_K77]
not_yet = '/html/body/div/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/fieldset/div[9]/strong'

def check_status(link):
    try:
        driver.get(link)
        text = driver.find_elements_by_xpath(not_yet)[0].text
        return True
    except:
        return False


while(True):
    for i in list:
        print(i)
        print(check_status(i))
        time.sleep(5)