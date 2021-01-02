from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def TranslateNumbers(cookies, price, numbers_notation):
    c = cookies.replace(',','')
    c = c.split(" ")
    exp = 3
    prefix = c[1]

    if prefix[0] == "c":
        cookies = c[0]
    else:
        prefix = prefix.split("\n")
        prefix = prefix[0]
        for notation in numbers_notation:
            exp += 3
            if prefix == notation:
                cookies = float(c[0]) * pow(10, exp)
                break

    p = price.replace(',', '')
    p = p.split(" ")
    exp = 3

    if len(p) == 1:
        price = p[0]
    else:
        for notation in numbers_notation:
            exp += 3
            if p[1] == notation:
                price = float(p[0]) * pow(10, exp)
                break
    return cookies, price

def SaveGame(driver):
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

        action.move_by_offset(484, 305).click()  #might need to change these numbers depending on your browser, but generally should work
        action.perform()
        time.sleep(2)

        save_area_text = driver.find_element_by_xpath('//*[@id="textareaPrompt"]').text
        with open('save.txt', 'w') as file:
            file.write(save_area_text)

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="promptOption0"]').click()
        print('Game saved!')
    except Exception:
        print('Game save failed. Script is gonna try save again later.')
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="close menuClose"]').click()

def LoadGame(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html")))
    time.sleep(4)
    driver.find_element_by_xpath('/html').send_keys(Keys.LEFT_CONTROL, 'O')
    time.sleep(2)
    with open('save.txt', 'r') as file:
        save_text = file.read()
        driver.find_element_by_xpath('//*[@id="textareaPrompt"]').send_keys(save_text)

    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="promptOption0"]').click()

    print('Game loaded!')
    time.sleep(2)

def GoldenCookie(driver):
    try:
        driver.find_element_by_xpath('//*[@id="shimmers"]/div').click()
    except:
        pass

def Shopping(driver, product_prices, number_of_cookies, numbers_notation):
    for item in product_prices:  # index of item in shop is on [0] and price is on [1]
        while True:
            cookies, price = TranslateNumbers(number_of_cookies.text, item[1].text, numbers_notation)
            if float(cookies) >= float(price):
                product = driver.find_element_by_xpath("//div[@id='product{}']".format(str(item[0])))
                product.click()
                name = driver.find_element_by_xpath("//div[@id='productName{}']".format(str(item[0]))).text
                print(name, 'has been bought!')
                time.sleep(0.3)
                continue
            break

def Upgrading(driver):
    try:
        e = driver.find_element_by_xpath("//div[@class='crate upgrade enabled']")
        e.click()
        print('Upgrade has been bought!')
    except:
        print('Not enough funds for upgrade!')

def CheckShop(driver, product_prices):
    try:
        e = driver.find_element_by_xpath("//div[@class='product locked disabled toggledOff']").get_attribute('id')
        product_prices.clear()
        for index in range(int(e[-1]) - 1, -1, -1):
            product_prices.append((index, driver.find_element_by_xpath("//span[@id='productPrice{}']".format(str(index)))))
        return True
    except:
        product_prices.clear()
        for index in range(17, -1, -1):
            product_prices.append((index, driver.find_element_by_xpath("//span[@id='productPrice{}']".format(str(index)))))
        return False


def Game(loops, small_click_loop, shop, save):
    PATH = 'C:\Program Files (x86)\chromedriver.exe' #put here path to your chromedriver.exe
    driver = webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    print(driver.title)

    LoadGame(driver)
    #Comment above line when you start new game.
    #If you start new game you have to also clear save.txt file.
    #If you want to load your own game, just paste your game save to "save.txt", save and run with uncommented line
    # Should click on the golden cookie if it is on screen
    product_prices = []
    numbers_notation = ["million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
                        "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion",
                        "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion",
                        "vigintillion"]
    shop_or_upgrade = True
    check_shop = True
    big_cookie = driver.find_element_by_xpath("//div[@id='bigCookie']")
    number_of_cookies = driver.find_element_by_xpath("//div[@id='cookies']")

    #Main loop of the game
    for i in range(1, loops):
        for j in range(small_click_loop):
            big_cookie.click()
        GoldenCookie(driver)
        #print(number_of_cookies.text)
        if i % shop == 0:
            if check_shop:
                check_shop = CheckShop(driver, product_prices)
            if shop_or_upgrade:
                Shopping(driver, product_prices, number_of_cookies, numbers_notation)
                shop_or_upgrade = False
            else:
                Upgrading(driver)
                shop_or_upgrade = True
        if i % save == 0:
            SaveGame(driver)

###STARTING PARAMETERS###
#SMALL_CLICK_LOOP - determines how many clicks in one "small loop" default is 100 and I recommend leaving this option at 100
#SHOP - #determines how many "small clicks" multiplied by this variable to perform, before trying to buy anything from shop or try to upgrade.
#25 means shopping every ~40sec
#50 means shopping every ~1:15
#SAVE - #determines how many "small clicks" multiplied by this variable to perform, before trying to save a game.
#50 means saving about every 1:20min
#100 means saving about every 2:30
#LOOPS - one loop is "SMALL_CLICK_LOOP" clicks on bigCookie, checks for shop and save.
#########################

SMALL_CLICK_LOOP = 100
SHOP = 50
SAVE = 100
LOOPS = 5000
Game(LOOPS, SMALL_CLICK_LOOP, SHOP, SAVE)