from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

Chrome.get('http://uitestingplayground.com/classattr')
Firefox.get('http://uitestingplayground.com/classattr')

for _ in range(3):
    blue_button = Chrome.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    blue_button = Firefox.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    Chrome.switch_to.alert.accept()
    Firefox.switch_to.alert.accept()