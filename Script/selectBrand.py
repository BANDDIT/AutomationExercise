from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def selectBrand(driver): 
    # 1. Buka halaman produk
    driver.get("https://automationexercise.com/products")
    driver.maximize_window()
    time.sleep(2)

    # 2. Klik setiap brand
    brand_links = driver.find_elements(By.CSS_SELECTOR, ".nav-stacked li a")
    urls = [el.get_attribute("href") for el in brand_links]

    for url in urls:
        driver.get(url)
        print(f"Mengunjungi brand: {url}")
        time.sleep(2)
    
    driver.quit()


#Setup Browser & Execute
chromeDriver = webdriver.Chrome()
selectBrand(chromeDriver)

firefoxDriver = webdriver.Firefox()
selectBrand(firefoxDriver)

safariDriver = webdriver.Safari()
selectBrand(safariDriver)
