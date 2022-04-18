from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="chromedriver")
driver2 = webdriver.Chrome(executable_path="chromedriver")
driver3 = webdriver.Chrome(executable_path="chromedriver")
driver4 = webdriver.Chrome(executable_path="chromedriver")

driver1.get("https://www.youtube.com/watch?v=DoYcVf11aeo&ab_channel=Artur_dru")
driver2.get("https://www.youtube.com/watch?v=DoYcVf11aeo&ab_channel=Artur_dru")
driver3.get("https://www.youtube.com/watch?v=DoYcVf11aeo&ab_channel=Artur_dru")
driver4.get("https://www.youtube.com/watch?v=DoYcVf11aeo&ab_channel=Artur_dru")

while True:
    sleep(10)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()