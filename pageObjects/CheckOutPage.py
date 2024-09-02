

from selenium.webdriver.common.by import By

class CheckOut:
    product_amount = (By.XPATH, "//tr/td[5]/p[@class='amount']")
    total_amount = (By.CLASS_NAME, "totAmt")
    inputPromo = (By.CLASS_NAME, "promoCode")
    promoButton = (By.CLASS_NAME, "promoBtn")

    def __init__(self, driver):
        self.driver = driver

    def select_product_amount(self):
        return self.driver.find_elements(*CheckOut.product_amount)

    def select_total_amount(self):
        return self.driver.find_element(*CheckOut.total_amount)

    def select_input_promo(self):
        return self.driver.find_element(*CheckOut.inputPromo)

    def select_input_button(self):
        return self.driver.find_element(*CheckOut.promoButton)
