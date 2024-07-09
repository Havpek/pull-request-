from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

Chrome.get('http://the-internet.herokuapp.com/entry_ad')
wait = WebDriverWait(Chrome, 10)
modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
close_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
close_button.click()

Firefox.get('http://the-internet.herokuapp.com/entry_ad')
wait = WebDriverWait(Firefox, 10)
modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
close_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
close_button.click()