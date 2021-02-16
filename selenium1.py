from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Opera(PATH)

driver.get("https://www.facebook.com")