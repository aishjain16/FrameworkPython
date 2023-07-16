from selenium.webdriver.common.by import By


class HomePage:

    shop=By.LINK_TEXT, "Shop"

    def __init__(self,driver):
        self.driver=driver

    def shopItem(self):
      return self.driver.find_element(*HomePage.shop)