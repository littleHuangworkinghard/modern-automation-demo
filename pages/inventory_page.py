from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    # 定位器
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")

    def get_page_title(self):
        """获取页面标题"""
        return self.get_element_text(self.PRODUCTS_TITLE)

    def add_first_item_to_cart(self):
        """添加第一个商品到购物车"""
        self.click_element((self.ADD_TO_CART_BUTTON[0], f"{self.ADD_TO_CART_BUTTON[1]}-sauce-labs-backpack"))

    def get_cart_count(self):
        """获取购物车商品数量"""
        try:
            return int(self.get_element_text(self.SHOPPING_CART))
        except:
            return 0