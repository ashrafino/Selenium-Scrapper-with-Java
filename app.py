from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)
url = 'https://www.jumia.ma/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        produit = request.form['text']

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        time.sleep(3)

        close = driver.find_element(By.XPATH, '//*[@id="pop"]/div/section/button')
        close.click()
        time.sleep(2)

        search = driver.find_element(By.XPATH, '//*[@aria-label="Rechercher"]')
        search.send_keys([produit])  # Convert produit to a list

        rechercher = driver.find_element(By.XPATH, '//*[@id="search"]/button')
        rechercher.click()

        # Scroll down until the end of the page
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

        product_names = []
        product_prices = []
        product_images = []

        while True:
            try:
                for product in driver.find_elements(By.XPATH, '//*[@class="name"]'):
                    product_names.append(product.text if product.text else "")

                for product in driver.find_elements(By.XPATH, '//*[@class="prc"]'):
                    product_prices.append(product.text if product.text else "")

                for product in driver.find_elements(By.XPATH, '//*[@class="img-c"]/img'):
                    product_images.append(product.get_attribute("src") if product.get_attribute("src") else "")

                break
            except StaleElementReferenceException:
                product_names = []
                product_prices = []
                product_images = []
                time.sleep(1)

        driver.quit()

        return render_template('index.html', produit=produit, product_names=product_names, product_prices=product_prices, product_images=product_images)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.1.106')
