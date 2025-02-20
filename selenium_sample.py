import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

with webdriver.Chrome() as driver:
    driver.get("https://google.co.jp")
    
    time.sleep(3)
    
    elements = driver.find_elements(By.NAME, "q")
    time.sleep(3)
    element = elements[0]
    element.send_keys("タイピング練習道場")
    element.send_keys(Keys.ENTER)
    
    time.sleep(30)
    
    driver.save_screenshot("screenshot.png")
