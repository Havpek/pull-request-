from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
Chrome.get('http://the-internet.herokuapp.com/inputs')
Firefox.get('http://the-internet.herokuapp.com/inputs')
input_field = Chrome.find_element(By.TAG_NAME, "input")
input_field = Firefox.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
input_field.clear()
input_field.send_keys("999")