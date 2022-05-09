from selenium import webdriver
search = input('enter the string you want to search for')
browser = webdriver.Chrome('chromedriver')
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" + search + "&start=" + str(i))