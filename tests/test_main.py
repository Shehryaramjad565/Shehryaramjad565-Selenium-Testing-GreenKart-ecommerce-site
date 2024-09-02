

# import time
#
# from pageObjects.HomePage import HomePage
# from utilities.BaseClass import Baseclass
#
# class TestExample(Baseclass):
#
#     def test_title(self):
#         # Create an instance of HomePage
#         log=self.getLogger()
#         homepage = HomePage(self.driver)
#
#         # Search for a product
#         homepage.Select().send_keys("st")
#
#         # Wait for the products to load
#         time.sleep(2)  # Better to use explicit wait here
#
#         # Locate all the individual products
#         product_elements = homepage.select_elements()
#
#         homepage.select_both_products(product_elements)
#         # Click on the cart icon
#         cart = homepage.select_cart_icon()
#         cart.click()
#
#         # Proceed to checkout
#         checkout = homepage.select_checkout_button()
#
#         # Validate the total amount
#         product_amount = checkout.select_product_amount()
#         list1 = []
#         for item in product_amount:
#             list1.append(int(item.text))
#             log.info("product amount are" + item.text)
#
#         total_price = checkout.select_total_amount()
#         total_price = int(total_price.text)
#         product_sum = sum(list1)
#
#         if total_price == product_sum:
#             log.info("Total price is the same")
#
#         self.VerifyLinkPresence('rahulshettyacademy')
#
#         promoButton = checkout.select_input_button()
#         promoButton.click()
#         time.sleep(8)
#         log.info(self.driver.title)








import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass

class TestExample(Baseclass):

    def test_title(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        # Search for a product
        homepage.Select().send_keys("st")

        # Wait for the products to load
        time.sleep(2)  # Better to use explicit wait here

        # Locate all the individual products
        product_elements = homepage.select_elements()

        homepage.select_both_products(product_elements)

        # Click on the cart icon
        cart = homepage.select_cart_icon()
        cart.click()

        # Proceed to checkout
        checkout = homepage.select_checkout_button()

        # Validate the total amount
        product_amount = checkout.select_product_amount()
        list1 = []
        for item in product_amount:
            list1.append(int(item.text))
            log.info("Product amount: " + item.text)

        total_price = checkout.select_total_amount()
        total_price = int(total_price.text)
        product_sum = sum(list1)

        # Assert that the total price is equal to the sum of product prices
        assert total_price == product_sum, f"Total price {total_price} does not match the sum of product prices {product_sum}"
        log.info("Total price is the same")

        # Verify the presence of the 'rahulshettyacademy' link
        self.VerifyLinkPresence('rahulshettyacademy')

        # Click the promo button
        promoButton = checkout.select_input_button()
        promoButton.click()

        time.sleep(8)
        log.info(self.driver.title)
