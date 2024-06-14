from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from tests_UI_oksana_selenium.pages.create_account_page import CreateNewAccount
from tests_UI_oksana_selenium.pages.eco_friendly_page import ProductChecker
from tests_UI_oksana_selenium.pages.sale_page import SaleChecker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    # driver = webdriver.Chrome(options=options)
    # yield driver
    # driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return ProductChecker(driver)


@pytest.fixture()
def sale_page(driver):
    return SaleChecker(driver)
