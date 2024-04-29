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
URL = "https://www.empleospublicos.cl/"
EMAIL_PATTERN = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
BUSQUEDA = "ingeniero"

class DataStructure:
    def __init__(self, data_list):
        
        # Initialize an empty dictionary to store the data
        self.data = {}

        # Extract and store values from the list
        self.data['Titulo'] = data_list[0]
        self.data['Organizacion'] = data_list[1]
        self.data['Ministerio'] = data_list[2]
        self.data['Ubicacion'] = data_list[3]
        self.data['URL'] = data_list[4]

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return f"Data: {self.data}"
    
def main():
    
    opts = Options()
    opts.add_argument(USER_AGENT)
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-extensions")
    # opts.add_argument("--headless")
    opts.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts
    )
    
    driver.get(url=URL)
    
    buscador_principal = driver.find_element(By.ID, "buscadorprincipal")
    buscador_principal.send_keys(BUSQUEDA)    
    buscador_principal.send_keys(Keys.ENTER)
    
    resultados = driver.find_elements(By.CLASS_NAME, "busqueda")
    
    final_data = []
    
    for index, resultado in enumerate(resultados):
        data_list = []
        div_number = index + 1
        a_etiquete = resultado.find_element(By.XPATH, '//div[{}]/div/div[1]/h3/a'.format(div_number))
        url_job = a_etiquete.get_attribute('href')
        
        # Create list of data with the data
        data_list = resultado.text.splitlines()
        data_list.pop()
        data_list.append(url_job)
        
        data = DataStructure(data_list)
        final_data.append(data)
    
    # Show results
    
    print('Scraping to {} is ended.'.format(URL))
    print('About searching: {} founded {} jobs.'.format(BUSQUEDA, len(final_data)))

    for index, data in enumerate(final_data):
        counter = index + 1
        print('{} {}'.format(counter, data))
        
    driver.quit()
    
if __name__ == '__main__':
    main()