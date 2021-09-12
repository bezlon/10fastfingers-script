from selenium import webdriver
import time
import keyboard

driver = webdriver.Chrome()

driver.get("https://10fastfingers.com/typing-test/english")
time.sleep(10)
words = driver.find_elements_by_xpath("//div[@id='row1']/span")

for e in words:
    keyboard.write(e.text)
    keyboard.press_and_release("space")
    #time.sleep(0.333)
    
time.sleep(100)