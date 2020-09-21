from selenium import webdriver
import time
import telegram
import random

driver = webdriver.Chrome("chromedriver/chromedriver.exe")

kevcase_899 = "https://smartstore.naver.com/hyotrade/products/4809552659"
kevcase_599 = "https://smartstore.naver.com/hyotrade/products/5006125821"
acat_x1 = "https://smartstore.naver.com/hyotrade/products/5092067009"
list = [kevcase_599, kevcase_899, acat_x1]

not_yet = '/html/body/div/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/fieldset/div[9]/strong'

telegram_token = ""
bot = telegram.Bot(token=telegram_token)

sff_gall = "https://gall.dcinside.com/mgallery/board/write/?id=sff"

def check_status(link):
    try:
        driver.implicitly_wait(5)
        driver.get(link)
        text = driver.find_elements_by_xpath(not_yet)[0].text
        if text == "이 상품은 현재 구매하실 수 없는 상품입니다.":
            return True
        else:
            return False
    except:
        return None
def send_msg(link):
    updates = bot.getUpdates()
    chat_id = updates[-1].message.chat_id
    bot.sendMessage(chat_id=chat_id, text=link)

def write_gall(message):
    driver.get(sff_gall)
    driver.find_elements_by_xpath('//*[@id="name"]')[0].send_keys('짭스트 알리미')
    time.sleep(1)
    driver.find_elements_by_xpath('//*[@id="password"]')[0].send_keys('q1w2e3r4t5y6')
    time.sleep(1)
    driver.find_elements_by_xpath('//*[@id="subject"]')[0].send_keys('효트 짭스트 입고 알림')
    time.sleep(1)
    driver.find_elements_by_xpath('//*[@id="write"]/div[1]/fieldset/div[3]/ul/li[1]')[0].click()
    time.sleep(random.randrange(0, 5))
    driver.find_elements_by_xpath('//*[@id="chk_html"]')[0].click()
    source_code = '<p>짭스트 알림</p><p><a href="'+message+'" target="_blank" class="tx-link">'+message+'</a><br></p>'
    driver.find_elements_by_xpath('//*[@id="tx_canvas_source"]')[0].send_keys(source_code)
    time.sleep(random.randrange(0, 3))
    driver.find_elements_by_xpath('//*[@id="chk_html"]')[0].click()
    time.sleep(random.randrange(0, 3))
    driver.find_elements_by_xpath('//*[@id="write"]/div[4]/button[2]')[0].click()
    time.sleep(15)
while(True):
    for i in list:
        print(i)
        write_gall(i)
        status = check_status(i)
        if status == False:
            send_msg(i)
        elif status == None:
            send_msg("Connection Error")
        time.sleep(30)
    time.sleep(1800)