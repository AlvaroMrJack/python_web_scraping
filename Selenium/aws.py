from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

USER_AGENT = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
URL_AWS = "https://aws.amazon.com/es/"
URL = "https://aws.amazon.com/es/pricing/"
BUSQUEDA = "Amazon Aurora"

def main():

    opts = Options()
    opts.add_argument(USER_AGENT)
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    opts.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )

    driver.get(url=URL_AWS)

    WebDriverWait(driver, 5)\
        .until(
            EC.element_to_be_clickable((By.CLASS_NAME, "m-nav-search-icon"))
        ).click()

    input_buscar = driver.find_element(By.NAME, "searchQuery")
    input_buscar.send_keys(BUSQUEDA)

    WebDriverWait(driver, 3)\
        .until(
            EC.element_to_be_clickable((By.CLASS_NAME, "tt-btn"))
        ).click()

    costo_exportacion = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[11]/div/div/div[26]/table/tbody/tr[3]/td[3]/b')
    print('Costo de exportacion de AWS Aurora es: {}'.format(costo_exportacion.text))

    driver.quit()

if __name__ == '__main__':
    main()