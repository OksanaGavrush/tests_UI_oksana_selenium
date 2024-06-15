from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from tests_UI_oksana_selenium.pages.create_account_page import CreateNewAccount
from tests_UI_oksana_selenium.pages.eco_friendly_page import ProductChecker
from tests_UI_oksana_selenium.pages.sale_page import SaleChecker


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск без GUI
    options.add_argument("--no-sandbox")  # Запуск в безопасной среде без использования песочницы
    options.add_argument("--disable-dev-shm-usage")  # Отключение использования /dev/shm
    options.add_argument("--disable-gpu")  # Отключение аппаратного ускорения
    options.add_argument(
        "--disable-features=NetworkService,NetworkServiceInProcess")  # Отключение некоторых функций сетевых сервисов
    options.add_argument("--disable-extensions")  # Отключение расширений
    options.add_argument("--disable-infobars")  # Отключение информационных строк

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return ProductChecker(driver)


@pytest.fixture()
def sale_page(driver):
    return SaleChecker(driver)
