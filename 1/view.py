from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.youtube.com/watch?v=DoYcVf11aeo&ab_channel=Artur_dru"
NEXT_BUTTON_XPATH = "//*[@id=""]/div[26]/div[2]/div[1]/button"
while True:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep()
    browser.refresh()

    browser.quit()
