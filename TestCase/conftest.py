import pytest
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


# def pytest_addoption(parser):
#     parser.addoption("--browser_name",action="store",default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    service_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj,options=options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver

    # yield
    # driver.close()

