from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def viewSpecificProduct(driver):
    # 1. Buka halaman produk
    driver.get("https://automationexercise.com/products") 
    driver.maximize_window()
    time.sleep(2)

    # 2. View Product
    css_selector =  ".choose ul li a"
    brand_links = driver.find_elements(By.CSS_SELECTOR, css_selector)
    urls = [el.get_attribute("href") for el in brand_links]

    for url in urls:   
        time.sleep(2) 
        driver.get(url)
        time.sleep(2)
        driver.back()

    time.sleep(5)

    driver.quit()

#Setup Browser & Execute
driver = webdriver.Chrome()
viewSpecificProduct(driver)

driver = webdriver.Firefox()
viewSpecificProduct(driver)

safariDriver = webdriver.Safari()
viewSpecificProduct(driver)