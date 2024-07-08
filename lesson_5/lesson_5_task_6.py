from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
Chrome.get('http://the-internet.herokuapp.com/login')
Firefox.get('http://the-internet.herokuapp.com/login')
input_name = Chrome.find_element(By.ID, "username").send_keys("tomsmith")
input_name = Firefox.find_element(By.ID, "username").send_keys("tomsmith")
input_pass = Chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
input_pass = Firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
button = Chrome.find_element(By.TAG_NAME, "button").click()
button = Firefox.find_element(By.TAG_NAME, "button").click()
