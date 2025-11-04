import pytest
import allure
from config.config import Config


@allure.story("登录功能测试")
class TestLogin:

    @allure.title("成功登录测试")
    def test_successful_login(self, driver, login_page, inventory_page):
        """测试成功登录场景"""
        with allure.step("打开登录页面"):
            driver.get(Config.BASE_URL)

        with allure.step("输入用户名和密码"):
            login_page.login(Config.STANDARD_USER, Config.PASSWORD)

        with allure.step("验证登录成功"):
            assert "inventory" in driver.current_url
            assert inventory_page.get_page_title() == "PRODUCTS"

    @allure.title("失败登录测试")
    def test_failed_login(self, driver, login_page):
        """测试失败登录场景"""
        with allure.step("打开登录页面"):
            driver.get(Config.BASE_URL)

        with allure.step("输入错误的密码"):
            login_page.login(Config.STANDARD_USER, "wrong_password")

        with allure.step("验证错误信息"):
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text


@allure.story("购物车功能测试")
class TestShoppingCart:

    @allure.title("添加商品到购物车")
    def test_add_item_to_cart(self, driver, login_page, inventory_page):
        """测试添加商品到购物车"""
        with allure.step("登录系统"):
            driver.get(Config.BASE_URL)
            login_page.login(Config.STANDARD_USER, Config.PASSWORD)

        with allure.step("添加商品到购物车"):
            inventory_page.add_first_item_to_cart()

        with allure.step("验证购物车数量"):
            assert inventory_page.get_cart_count() == 1