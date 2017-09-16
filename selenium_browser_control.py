from selenium import webdriver
path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
browser=webdriver.Chrome(path)
browser.get("http://www.yahoo.com")
browser.close()
browser.quit()
type(browser)
