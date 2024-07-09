from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(Chrome, 40, 0.1)

Chrome.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait.until(EC.text_to_be_present_in_element(
    (By.ID, "text"), "Done"))
get_attribute = Chrome.find_element(
    By.ID, "award").get_attribute("src")
print(get_attribute)