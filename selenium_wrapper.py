import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import keyboard

class SeleniumTypingPage:
    def OpenTypingPage():
        with webdriver.Chrome() as driver:
            driver.get("https://keyboard-dojo.net/")
            
            time.sleep(3)
            
            elements = driver.find_elements(By.ID, "start")
            element = elements[0]
            element.click()
            
            startflg = False            
            running = True
            lastQuestion = ""
            try:
                while running:
                    elements = driver.find_elements(By.ID, "question")
                    if elements:
                        startflg = True
                        element = elements[0]
                        if element.text != lastQuestion:
                            # print(element.text)
                            inputElements = driver.find_elements(By.ID, "input_area")
                            if inputElements:
                                inputElement = inputElements[0]
                                inputElement.send_keys(element.text)
                                time.sleep(0.5)
                                inputElement.send_keys(Keys.ENTER)
                                time.sleep(1.5)
                    else:
                        if startflg:
                            running = False
            except:
                pass
            time.sleep(2)
            driver.save_screenshot("screenshot.png")

            # ESC キーが押されるまで待機
            time.sleep(8)
                
if __name__ == "__main__":
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
