from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    Chrome.get(' http://the-internet.herokuapp.com/add_remove_elements/')
    Firefox.get(' http://the-internet.herokuapp.com/add_remove_elements/')
    for _ in range(5):
       add_button = Chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
       add_button = Firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
       chrome_delete_buttons = Chrome.find_elements("xpath", '//button[text()="Delete"]')
       firefox_delete_buttons = Firefox.find_elements("xpath", '//button[text()="Delete"]')
    print(
        f"Список кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"Список кнопок Delete в Firefox: {len(firefox_delete_buttons)}")
except Exception as ex:
    print(ex)
finally:
    Chrome.quit()
    Firefox.quit()
