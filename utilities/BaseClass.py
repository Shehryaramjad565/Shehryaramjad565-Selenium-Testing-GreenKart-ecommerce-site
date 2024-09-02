# import pytest
#
# @pytest.mark.usefixtures('setup')
# class Baseclass:
#     pass






# # BaseClass.py
import inspect
import logging

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('setup')
class Baseclass:
    def VerifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        inputPromo = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "promoCode")))
        # inputPromo.send_keys("rahulshettyacademy")
        inputPromo.send_keys(text)


    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger