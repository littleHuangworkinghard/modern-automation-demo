import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture"""
    chrome_options = Options()
    if Config.HEADLESS:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    """登录页面fixture"""
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    """库存页面fixture"""
    from pages.inventory_page import InventoryPage
    return InventoryPage(driver)