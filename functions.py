from selenium import webdriver 
from selenium.webdriver.common.by import By

# >> for running in headless mode

# from selenium.webdriver.firefox.options import Options
# firefox_options = Options()
# firefox_options.headless = True
# driver = webdriver.Firefox(options=firefox_options, executable_path=PATH)

# <<

driver = webdriver.Firefox()

driver.get("URL")

# driver.refresh()
# driver.save_screenshot(capture_path)

def send_data(xpath, keys):
    driver.find_element(By.XPATH, xpath).clear() # clears input field, if any text is pre-written
    driver.find_element(By.XPATH, xpath).send_keys(keys)

def click_element(xpath):
    driver.find_element(By.XPATH, xpath).click()

def getText(xpath):
    return driver.find_element(By.XPATH, xpath).text
