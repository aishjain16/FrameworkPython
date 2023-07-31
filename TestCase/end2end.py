from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from PageObject.ChechOutPage import CheckOutPage

class TestOne(BaseClass):

    def test_e2e(self):
        homepage=HomePage(self.driver)
        homepage.shopItem().click()
        checkOutPage=CheckOutPage(self.driver)
        # checkOutPage.getcardtitle()
        # checkOutPage.getCardFooter()


        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # list = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        list=checkOutPage.getcardtitle()
        # i=-1
        # for card in list:
        #     i=i+1
        #     cardtext=card.text
        #     print(cardtext)
        #     if cardtext == "Blackberry":
        #         checkOutPage.getCardFooter().click()
        for ele in list:
            # product = (ele.text)
            product=ele.find_element(By.XPATH, "div/h4/a").text
            print(product)
            if product == "Blackberry":
                ele.find_element(By.XPATH,"div/button").click()

        checkOutPage.clickoncheckout().click()