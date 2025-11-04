import pytest
import requests
import allure
from config.config import Config


@allure.story("用户API测试")
class TestUserAPI:

    @allure.title("获取用户列表")
    def test_get_users(self):
        """测试获取用户列表API"""
        with allure.step("发送GET请求获取用户列表"):
            response = requests.get(f"{Config.API_BASE_URL}/users?page=2")

        with allure.step("验证响应状态码"):
            assert response.status_code == 200

        with allure.step("验证响应数据结构"):
            data = response.json()
            assert "page" in data
            assert "data" in data
            assert len(data["data"]) > 0

    @allure.title("创建新用户")
    def test_create_user(self):
        """测试创建用户API"""
        with allure.step("准备测试数据"):
            user_data = {
                "name": "morpheus",
                "job": "leader"
            }

        with allure.step("发送POST请求创建用户"):
            response = requests.post(f"{Config.API_BASE_URL}/users", json=user_data)

        with allure.step("验证响应状态码"):
            assert response.status_code == 201

        with allure.step("验证返回的用户信息"):
            data = response.json()
            assert data["name"] == user_data["name"]
            assert data["job"] == user_data["job"]
            assert "id" in data
            assert "createdAt" in data

    @allure.title("用户登录测试")
    def test_user_login(self):
        """测试用户登录API"""
        with allure.step("发送登录请求"):
            login_data = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
            response = requests.post(f"{Config.API_BASE_URL}/login", json=login_data)

        with allure.step("验证登录成功"):
            assert response.status_code == 200
            data = response.json()
            assert "token" in data