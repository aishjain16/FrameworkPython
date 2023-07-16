from selenium.webdriver.common.by import By


class CheckOutPage:
    cardtitle = By.XPATH, "//div[@class='card h-100']"
    cardbutton = By.XPATH, "div/button"

    def __init__(self,driver):
        self.driver=driver

    # list=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

    def getcardtitle(self):
        return self.driver.find_elements(*CheckOutPage.cardtitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardbutton)
