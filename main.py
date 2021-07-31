from selenium import webdriver

chrome_driver_path = "/Users/benbauer/Documents/VSCode/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.bestbuy.com/site/msi-gf65-15-6-144hz-gaming-laptop-intel-core-i5-nvidia-geforce-rtx3060-512gb-ssd-8gb-memory-black/6456144.p?skuId=6456144")
stock = driver.find_element_by_class_name("fulfillment-fulfillment-summary")
print(stock.text)
driver.quit()

