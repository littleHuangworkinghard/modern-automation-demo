from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """查找元素并等待"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def take_screenshot(self, name):
        """截图"""
        self.driver.save_screenshot(f"screenshots/{name}.png")