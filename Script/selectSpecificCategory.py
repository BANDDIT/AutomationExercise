from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def selectSpecificCategory(driver): 
    # 1. Buka halaman produk
    driver.get("https://automationexercise.com/products") 
    driver.maximize_window()
    time.sleep(2)

    # 2. Klik setiap Specific Category
    panelDefault = driver.find_elements(By.CSS_SELECTOR, ".panel-default")
    panelCount = len(panelDefault)

    for i in range(panelCount) : 
        specificCategory = panelDefault[i].find_elements(By.CSS_SELECTOR, ".panel-body ul li a")
        urlSpecificCategory = [el.get_attribute("href") for el in specificCategory]

        for url in urlSpecificCategory : 
            driver.get(url)

            panelDefault = driver.find_elements(By.CSS_SELECTOR, ".panel-default")
            category = panelDefault[i].find_element(By.CSS_SELECTOR, '.panel-title a')
            category.click()

            time.sleep(2)

    driver.quit()

#Setup Browser & Execute
driver = webdriver.Chrome()
selectSpecificCategory(driver)

driver = webdriver.Firefox()
selectSpecificCategory(driver)

safariDriver = webdriver.Safari()
selectSpecificCategory(driver)