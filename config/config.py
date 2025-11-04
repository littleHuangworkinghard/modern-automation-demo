import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = "https://www.saucedemo.com"
    API_BASE_URL = "https://reqres.in/api"
    STANDARD_USER = os.getenv('STANDARD_USER', 'standard_user')
    PASSWORD = os.getenv('PASSWORD', 'secret_sauce')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
