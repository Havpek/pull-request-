from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

count = 0
Chrome.get("http://uitestingplayground.com/dynamicid")
Firefox.get("http://uitestingplayground.com/dynamicid")

blue_button = Chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
blue_button = Firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
for _ in range(3):
    blue_button = Chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = Firefox.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1
print(count)