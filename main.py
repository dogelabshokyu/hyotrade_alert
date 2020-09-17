from selenium import webdriver
import time
import telegram

driver = webdriver.Chrome("chromedriver/chromedriver.exe")

kevcase_899 = "https://smartstore.naver.com/hyotrade/products/4809552659"
kevcase_599 = "https://smartstore.naver.com/hyotrade/products/5006125821"
acat_x1 = "https://smartstore.naver.com/hyotrade/products/5092067009"
list = [kevcase_599, kevcase_899, acat_x1]

not_yet = '/html/body/div/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/fieldset/div[9]/strong'

telegram_token = ""

bot = telegram.Bot(token=telegram_token)

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

while(True):
    for i in list:
        print(i)
        status = check_status(i)
        if status == False:
            send_msg(i)
        elif status == None:
            send_msg("Connection Error")
    time.sleep(1800)