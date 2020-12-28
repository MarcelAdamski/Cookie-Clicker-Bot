from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pickle

def TranslateNumbers(cookies, price):
    c = cookies.replace(',','')
    c = c.split(" ")
    if len(c) == 1:
        cookies = c[0]
    elif c[1] == "million":
        cookies = float(c[0]) * pow(10,6)
    elif c[1] == "billion":
        cookies = float(c[0]) * pow(10,9)
    elif c[1] == "trillion":
        cookies = float(c[0]) * pow(10,12)
    elif c[1] == "quadrillion":
        cookies = float(c[0]) * pow(10,15)
    elif c[1] == "quintillion":
        cookies = float(c[0]) * pow(10,18)
    elif c[1] == "sextillion":
        cookies = float(c[0]) * pow(10,21)
    elif c[1] == "septillion":
        cookies = float(c[0]) * pow(10,24)
    elif c[1] == "octillion":
        cookies = float(c[0]) * pow(10,27)
    elif c[1] == "nonillion":
        cookies = float(c[0]) * pow(10,30)
    elif c[1] == "decillion":
        cookies = float(c[0]) * pow(10,33)
    elif c[1] == "undecillion":
        cookies = float(c[0]) * pow(10,36)
    elif c[1] == "duodecillion":
        cookies = float(c[0]) * pow(10,39)
    elif c[1] == "tredecillion":
        cookies = float(c[0]) * pow(10,42)
    elif c[1] == "quattuordecillion":
        cookies = float(c[0]) * pow(10,45)
    elif c[1] == "quindecillion":
        cookies = float(c[0]) * pow(10,48)
    elif c[1] == "sexdecillion":
        cookies = float(c[0]) * pow(10,51)
    elif c[1] == "septendecillion":
        cookies = float(c[0]) * pow(10,54)
    elif c[1] == "octodecillion":
        cookies = float(c[0]) * pow(10,57)
    elif c[1] == "novemdecillion":
        cookies = float(c[0]) * pow(10,60)
    elif c[1] == "vigintillion":
        cookies = float(c[0]) * pow(10,63)

    p = price.replace(',', '')
    p = p.split(" ")

    if len(p)==1:
        price = p[0]
    elif p[1] == "million":
        price = float(c[0]) * pow(10, 6)
    elif p[1] == "billion":
        price = float(c[0]) * pow(10, 9)
    elif p[1] == "trillion":
        price = float(c[0]) * pow(10, 12)
    elif p[1] == "quadrillion":
        price = float(c[0]) * pow(10, 15)
    elif p[1] == "quintillion":
        price = float(c[0]) * pow(10, 18)
    elif p[1] == "sextillion":
        price = float(c[0]) * pow(10, 21)
    elif p[1] == "septillion":
        price = float(c[0]) * pow(10, 24)
    elif p[1] == "octillion":
        price = float(c[0]) * pow(10, 27)
    elif p[1] == "nonillion":
        price = float(c[0]) * pow(10, 30)
    elif p[1] == "decillion":
        price = float(c[0]) * pow(10, 33)
    elif p[1] == "undecillion":
        price = float(c[0]) * pow(10, 36)
    elif p[1] == "duodecillion":
        price = float(c[0]) * pow(10, 39)
    elif p[1] == "tredecillion":
        price = float(c[0]) * pow(10, 42)
    elif p[1] == "quattuordecillion":
        price = float(c[0]) * pow(10, 45)
    elif p[1] == "quindecillion":
        price = float(c[0]) * pow(10, 48)
    elif p[1] == "sexdecillion":
        price = float(c[0]) * pow(10, 51)
    elif p[1] == "septendecillion":
        price = float(c[0]) * pow(10, 54)
    elif p[1] == "octodecillion":
        price = float(c[0]) * pow(10, 57)
    elif p[1] == "novemdecillion":
        price = float(c[0]) * pow(10, 60)
    elif p[1] == "vigintillion":
        price = float(c[0]) * pow(10, 63)
    return cookies, price

PATH = 'C:\Program Files (x86)\chromedriver.exe'
cookies_location = r"C:\Users\Marcel\PycharmProjects\selenium_04_cookie_clicker\cookies.txt"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

#driver.implicitly_wait(5)
#loading
WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "/html")))
time.sleep(4)
driver.find_element_by_xpath('/html').send_keys(Keys.LEFT_CONTROL, 'O')
time.sleep(2)
with open('save.txt', 'r') as file:
    save_text = file.read()
    driver.find_element_by_xpath('//*[@id="textareaPrompt"]').send_keys(save_text)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="promptOption0"]').click()

print('Game loaded !')
time.sleep(2)

#initalising variables
product_prices=[]
shop_or_upgrade = True
big_cookie = driver.find_element_by_xpath("//div[@id='bigCookie']")
number_of_cookies = driver.find_element_by_xpath("//div[@id='cookies']")
#starting script. script is saving about every 60s (or so)
for i in range(1, 5000):
    for j in range(50):
        big_cookie.click()
    cookies = number_of_cookies.text.split(" ")[0]
    print(cookies)

    if i%10 == 0:
        e = driver.find_element_by_xpath("//div[@class='product locked disabled toggledOff']").get_attribute('id')
        product_prices.clear()
        for index in range(int(e[-1]) - 1, -1, -1):
            product_prices.append((index, driver.find_element_by_xpath("//span[@id='productPrice{}']".format(str(index)))))
        if shop_or_upgrade:
            for item in product_prices: #index of item in shop is on [0] and price is on [1]
                print(item[0], item[1].text)
                while True:
                    cookies = number_of_cookies.text.split(" ")[0]
                    cookies, price = TranslateNumbers(cookies, item[1].text)
                    print(int(cookies), int(price))
                    if int(cookies) >= int(price):
                        product = driver.find_element_by_xpath("//div[@id='product{}']".format(str(item[0])))
                        product.click()
                        name = driver.find_element_by_xpath("//div[@id='productName{}']".format(str(item[0]))).text
                        print(name,'has been bought!')
                        time.sleep(0.3)
                        continue
                    break
            shop_or_upgrade = False
        else:
            try:
                e = driver.find_element_by_xpath("//div[@class='crate upgrade enabled']")
                e.click()
                print('Upgrade has been bought!')
            except:
                print('Upgrade not found or not enough funds!')
            shop_or_upgrade = True
    if i%100 == 0: #200 is every 1:55m #500 is every 5:40
        try:
            resetPosition = ActionChains(driver)
            action = ActionChains(driver)
            driver.find_element_by_xpath("//div[@id='prefsButton']").click()
            time.sleep(2)
            body = driver.find_element_by_xpath('/html/body')
            time.sleep(2)
            resetPosition.move_to_element_with_offset(body, 0, 0)
            resetPosition.perform()
            time.sleep(2)
            action.move_by_offset(484,305).click()  # might need to change these numbers, just run once with the above uncommented to know what to put in.
            action.perform()
            time.sleep(2)

            save_area_text = driver.find_element_by_xpath('//*[@id="textareaPrompt"]').text
            with open('save.txt', 'w') as file:
                file.write(save_area_text)

            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="promptOption0"]').click()
            print('Game saved+!')
        except Exception as e:
            print('Game save failed. Script is gonna try save again later.')
        time.sleep(5)
        driver.find_element_by_xpath('//div[@class="close menuClose"]').click()
#driver.quit()
