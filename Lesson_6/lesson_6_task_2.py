from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

Chrome.get('http://uitestingplayground.com/textinput')
button_name = Chrome.find_element("id", "newButtonName").send_keys("Rise")
confirm_button_name = Chrome.find_element("id", "updatingButton").click()
new_button_name = Chrome.find_element("id", "updatingButton").text
print(new_button_name)