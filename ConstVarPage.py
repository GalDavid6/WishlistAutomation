# This page purpose is to hold all the Const Var to keep the rest of the code clean and simple.

# UserInfo to sign in the website
account = "userName"
pw = "userPW"

# Website URL
Url = "https://my.asos.com/identity/"

# XPath
id_email = "//*[@id='EmailAddress']"
id_pw = "//*[@id='Password']"
id_signin = "//*[@id='signin']"
id_main_menu = "//*[@id='app']/div/div/div/div[1]/header/div/div/div[1]/div/a/img"
id_wishlist = "//*[@id='chrome-sticky-header']/div[1]/div/ul/li[2]/a/span"
id_discount_item = "//*[@class= 'productDiscount_mFttu productDiscount_Onc93']"

# Strings
no_Sale = "No items on sale right now."
Sale = "Go check your wishlist, Items on sale!!"

# WhatsApp Group ID, WhatsApp sending msg feature
WhatsApp_groupID = "Whatsapp Group ID"

# if getting ask "approve you are not robot" use this
# approve im not a robot (optional)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, id_signin)))
# element.click()
