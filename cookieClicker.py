import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def importFile(driver):
    with open('cookieClicker.txt') as f:
        lines = f.readlines()

    print(lines)
    options = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[1]/div[1]/div")
    options.click()
    print("options bitti")

    importt = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[2]")
    importt.click()
    print("importt bitti")

    textArea = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]/textarea")
    textArea.send_keys(lines)
    print("textArea bitti")

    textArea.send_keys(Keys.ENTER)

    # load = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[2]/a[1]")
    # load.click()
    #
    # print("load bitti")
    time.sleep(2)
    close = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[1]")
    close.click()

    print("close bittiiiiiiiiii")


def saveFile(driver):
    try:
        time.sleep(1)
        options = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[1]/div[1]/div")
        options.click()
        time.sleep(1)
        exportFile = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
        exportFile.click()
        time.sleep(1)
        theText = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]/textarea")
        lines = theText.text
        time.sleep(1)
        with open('cookieClicker.txt', 'w') as f:
            f.write(lines)
        time.sleep(1)
        allDone = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[12]/div/div[1]/div[2]/a")
        allDone.click()
        time.sleep(1)
        close = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[18]/div[2]/div[4]/div[1]")
        close.click()
        time.sleep(1)
        print("kaydettimm")
    except:
        print("ciktim")
        pass


def execute_app():
    PATH = "/home/burakkutlu/chromedriver_linux64/chromedriver"

    driver = webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    # driver.maximize_window()
    driver.implicitly_wait(3)

    try:
        language = driver.find_element(By.ID, "langSelect-EN")
        language.click()
    except:
        pass

    driver.implicitly_wait(15)
    time.sleep(8)
    importFile(driver)
    driver.implicitly_wait(5)

    cookie = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[15]/div[8]/button")

    hasStoreOpened = False

    turn_count = 0

    try:
        GotIt = driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
        GotIt.click()
    except:
        pass

    prevLockedProducts = 20
    totalProducts = 20

    while True:
        turn_count = turn_count + 1

        if turn_count >= 1000 and turn_count % 1000 == 0:
            print("save'e girdim")
            saveFile(driver)

        if hasStoreOpened and turn_count % 100 == 0:
            try:
                upgrade = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[19]/div[3]/div[5]/div[1]")
                if upgrade:
                    # upgrade.click()
                    store_upgrade_actions = ActionChains(driver)
                    store_upgrade_actions.move_to_element(upgrade)
                    store_upgrade_actions.click()
                    store_upgrade_actions.perform()
            except:
                pass

        try:
            if prevLockedProducts != 0:
                # print("locked sayiyom")
                lockedProducts = driver.find_elements(By.CLASS_NAME, "product.locked.disabled.toggledOff")

            # print("sayma bittiii")
            productsNeg = driver.find_elements(By.CLASS_NAME, "product.unlocked.disabled")
            prevLockedProducts = len(lockedProducts)
            # print("len(productsNeg): ", len(productsNeg))

            # print("totalProducts - prevLockedProducts:", totalProducts - prevLockedProducts)

            if len(productsNeg) != totalProducts - prevLockedProducts - 2:
                products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
                hasStoreOpened = True
                # print("productsNeg[0]:", productsNeg[0])
                # print("products[0]:", products[0])

                idPos = products[len(products) - 1].get_attribute("id")
                # print("idPos: ", idPos)
                toUpgrade = driver.find_element(By.ID, idPos)

                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(toUpgrade)
                upgrade_actions.click()
                upgrade_actions.perform()
        except:
            print("alamadimmmmmmm")
            pass

        try:
            cookie.click()
        except:
            print("olmadi")
            pass

def main():
    execute_app()


if __name__ == '__main__':
    main()
