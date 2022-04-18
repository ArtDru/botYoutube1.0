from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

useragent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")


driver1 = webdriver.Chrome(executable_path="chromedriver")
driver2 = webdriver.Chrome(executable_path="chromedriver")
driver3 = webdriver.Chrome(executable_path="chromedriver")
driver4 = webdriver.Chrome(executable_path="chromedriver")

driver1.get("https://youtu.be/PCLtRS4Kqqg")
driver2.get("https://youtu.be/PCLtRS4Kqqg")
driver3.get("https://youtu.be/PCLtRS4Kqqg")
driver4.get("https://youtu.be/PCLtRS4Kqqg")


while True:
    time.sleep(90)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
