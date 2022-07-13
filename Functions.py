from WebDriverCFG import *
from ConstVarPage import *
import pywhatkit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def sendwhatsapp(s):
    pywhatkit.sendwhatmsg_to_group_instantly(WhatsApp_groupID, s)


def checkwishlist():
    # Open website
    driver.get(Url)

    # log in
    driver.find_element(By.XPATH, id_email).send_keys(account)
    driver.find_element(By.XPATH, id_pw).send_keys(pw)
    driver.find_element(By.XPATH, id_signin).click()

    # main menu
    wait.until(EC.presence_of_element_located((By.XPATH, id_main_menu)))
    driver.find_element(By.XPATH, id_main_menu).click()

    # wish list
    wait.until(EC.presence_of_element_located((By.XPATH, id_wishlist)))
    driver.find_element(By.XPATH, id_wishlist).click()

    # creating a list including all items with discount
    wait.until(EC.presence_of_all_elements_located((By.XPATH, id_discount_item)))
    discount_items = driver.find_elements(By.XPATH, id_discount_item)
    driver.quit()

    return len(discount_items)
