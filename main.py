from selenium import webdriver

chrome_driver_path = "/Users/benbauer/Documents/VSCode/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

driver.quit()

