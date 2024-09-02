#



from selenium.webdriver.common.by import By
from pageObjects.CheckOutPage import CheckOut

class HomePage:

    shop = (By.CLASS_NAME, "search-keyword")
    products = (By.XPATH, "//div[@class='products']")
    product_element = (By.XPATH, ".//div[@class='product']")
    add_to_cart_button = (By.XPATH, ".//div[@class='product-action']/button")
    checkout_button = (By.XPATH, "//div[@class='cart-preview active']//button[contains(text(), 'PROCEED TO CHECKOUT')]")
    cart_icon = (By.CLASS_NAME, "cart-icon")

    def __init__(self, driver):
        self.driver = driver

    def Select(self):
        return self.driver.find_element(*HomePage.shop)

    def select_product(self):
        return self.driver.find_element(*HomePage.products)

    def select_elements(self):
        return self.driver.find_elements(*HomePage.product_element)

    def select_add_to_cart(self, product_item):
        return product_item.find_element(*HomePage.add_to_cart_button)

    def select_checkout_button(self):
        self.driver.find_element(*HomePage.checkout_button).click()
        return CheckOut(self.driver)

    def select_cart_icon(self):
        return self.driver.find_element(*HomePage.cart_icon)

    def select_both_products(self,product_elements):
        for item in product_elements:
            # Locate the product name
            product_name = item.find_element(By.XPATH, ".//h4").text
            if product_name == "Strawberry - 1/4 Kg":
                # Locate and click the 'Add to Cart' button
                add_to_cart_button = self.select_add_to_cart(item)
                add_to_cart_button.click()
                break  # Stop the loop after clicking the button

        for item in product_elements:
            # Locate the product name
            product_name = item.find_element(By.XPATH, ".//h4").text
            if product_name == "Pista - 1/4 Kg":
                # Locate and click the 'Add to Cart' button
                add_to_cart_button = self.select_add_to_cart(item)
                add_to_cart_button.click()
                break  # Stop the loop after clicking the button
