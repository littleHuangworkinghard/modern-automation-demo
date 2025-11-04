from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # 定位器
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, username, password):
        """登录操作"""
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """获取错误信息"""
        return self.get_element_text(self.ERROR_MESSAGE)