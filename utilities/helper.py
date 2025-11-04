import json
import random
import string

def generate_random_string(length=8):
    """生成随机字符串"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_email():
    """生成随机邮箱"""
    return f"test_{generate_random_string()}@example.com"

def read_test_data(file_path):
    """读取测试数据文件"""
    with open(file_path, 'r') as file:
        return json.load(file)