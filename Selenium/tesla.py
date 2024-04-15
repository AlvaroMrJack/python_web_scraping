from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

import re

USER_AGENT = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
URL = "https://www.tesla.com/"
EMAIL_PATTERN = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"

def main():
    
    opts = Options()
    opts.add_argument(USER_AGENT)
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )
    
    driver.get(url=URL)
    
    sleep(2)
    
    ActionChains(driver)\
        .send_keys(Keys.ESCAPE)\
        .perform()
    
    sleep(2)
    
    footer_logo = driver.find_element(By.CLASS_NAME, "tds-footer-item")

    ActionChains(driver)\
        .scroll_to_element(footer_logo)\
        .perform()

    WebDriverWait(driver, 3)\
        .until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Contact"))
        ).click()
    
    sleep(2)
    
    body = driver.find_element(By.TAG_NAME, "body")
    emails = re.findall(EMAIL_PATTERN, body.text)
    return_text = "Contact emails: {}".format(', '.join(emails))
    
    print(return_text)
    
    driver.quit()
    
if __name__ == '__main__':
    main()