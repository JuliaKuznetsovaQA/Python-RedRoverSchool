import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"

@pytest.fixture
def auth_token():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=auth_data)
    token = response.json()['token']
    yield token

@pytest.fixture
def create_booking():
        payload = {
            "firstname": "Max",
            "lastname": "Smith",
            "totalprice": 1258,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-03-01",
                "checkout": "2024-03-12"
            },
            "additionalneeds": "Additional bed"
            }
        result = requests.post(base_url, json=payload)
        print(result.json())
        booking_id = result.json()['bookingid']
        yield booking_id

