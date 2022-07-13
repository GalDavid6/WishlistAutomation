# WebDriver configurator

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# Enable logging on chrome, maxsize window & create driver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# Chrome ver 103 have bug with web driver so instead i used chrome 104 beta
# remove the line after if you are using another version of chrome
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"

driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                     'Chrome/85.0.4183.102 Safari/537.36'})

#  will be use for wait condition
wait = WebDriverWait(driver, 10)

# more CFG options
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (X11; Linux x86_64)'
#                                                         'AppleWebKit/537.36 (KHTML, like Gecko)'
#                                                         'Chrome/33.0.1750.517 Safari/537.36'})
