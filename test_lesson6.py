import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"


@pytest.fixture(scope='module')
def auth_token():
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=auth_data)
    token = response.json()['token']
    yield token

def summa(x, y):
    return x + y

@pytest.mark.skip
def test_equal():
    assert summa(3, 5) == 8

@pytest.mark.skip
def test_negative():
    assert summa(5, 6) == 7

@pytest.mark.regression
def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200

@pytest.fixture(scope='module')
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

@pytest.mark.smoke
def test_check_created_booking(create_booking):
    result = requests.get(f"{base_url}/{create_booking}")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == "Max"

def test_get_booking_by_id(create_booking):
    response = requests.get(f'{base_url}/{create_booking}')
    response_data = response.json()
    expected_keys = [
        'firstname',
        'lastname',
        'totalprice',
        'depositpaid',
        'bookingdates',
        'additionalneeds'
    ]
    print(response_data)
    assert response.status_code == 200
    for key in expected_keys:
        assert key in response_data.keys()
    assert len(expected_keys) == len(response_data.keys())

@pytest.mark.regression
def test_update_booking(auth_token, create_booking):
    token = {'Cookie': f'token={auth_token}'}
    payload = {
        "firstname": "Andrew",
        "lastname": "Smith",
        "totalprice": 1258,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-12"
        },
        "additionalneeds": "Lunch"
        }
    response = requests.put(f'{base_url}/{create_booking}', json=payload, headers=token)
    assert response.status_code == 200
    response2 = requests.get(f'{base_url}/{create_booking}')
    print(response2.json())
    assert response2.json()['firstname'] == 'Andrew'
    assert response2.json()['additionalneeds'] == 'Lunch'

def test_patch(auth_token, create_booking):
    token = {'Cookie': f'token={auth_token}'}
    payload = {
        "firstname": "Julia"
        }
    response = requests.patch(f'{base_url}/{create_booking}', json=payload, headers=token)
    assert response.status_code == 200
    response2 = requests.get(f'{base_url}/{create_booking}')
    print(response2.json())
    assert response2.json()['firstname'] == 'Julia'

def test_delete(create_booking, auth_token):
    token = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{base_url}/{create_booking}', headers=token)
    assert response.status_code == 201
    response2 = requests.get(f'{base_url}/{create_booking}')
    assert response2.status_code == 404
    print(response2.status_code)

def test_options():
    response = requests.options(base_url)
    assert response.status_code == 200
    print(response.text)

def test_headers():
    response = requests.head(base_url)
    assert response.status_code == 200
    print(response.headers)