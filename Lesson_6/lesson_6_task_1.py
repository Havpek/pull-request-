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
wait = WebDriverWait(Chrome, 40, 0.1)
wait = WebDriverWait(Firefox, 40, 0.1)
Chrome.get('http://uitestingplayground.com/ajax')
Firefox.get('http://uitestingplayground.com/ajax')
blue_button = Chrome.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
blue_button = Firefox.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
text_from_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))).text
print(text_from_content)