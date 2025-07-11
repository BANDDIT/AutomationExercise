from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def addToCart(driver) : 
    # 1. Buka halaman produk
    driver.get("https://automationexercise.com/products")  # Ganti dengan URL halaman produk sebenarnya
    driver.maximize_window()
    time.sleep(2)


    # 2. Klik semua tombol "Add to Cart"
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart")
    #"//button[contains(text(), 'Add to cart')]")

    for button in add_to_cart_buttons:
        try:
            button.click()
            time.sleep(3)  # beri delay kecil agar tidak terlalu cepat
            continue_shopping_buttons = driver.find_element(By.CSS_SELECTOR, ".close-modal")
            continue_shopping_buttons.click()
            time.sleep(3)  # beri delay kecil agar tidak terlalu cepat
        except:
            print("Gagal klik tombol.")

    # 3. Pergi ke halaman keranjang
    cart_button = driver.find_element(By.LINK_TEXT, "Cart")  # Ganti sesuai selector di website kamu
    cart_button.click()

    # Tunggu beberapa detik untuk melihat hasilnya
    time.sleep(150)

    # Selesai
    driver.quit()

#Setup Browser & Execute
driver = webdriver.Chrome()
addToCart(driver)

driver = webdriver.Firefox()
addToCart(driver)

driver = webdriver.Safari()
addToCart(driver)
