import random

import requests
import pytest

base_url = "https://petstore.swagger.io/v2/pet"

@pytest.fixture(scope='module')
def test_create_pet():
    pet_id = random.randint(1000, 10000)
    with open('pet_id.txt', 'w', encoding='utf-8') as f:
        f.write(f'{pet_id}')
    payload = {
          "id": pet_id,
          "category": {
            "id": 11122,
            "name": "cat"
          },
          "name": "Pushok",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "favourite"
        }
    response = requests.post(base_url, json=payload)
    print(response.status_code)
    print(response.json()['id'])
    print(response.json()['name'])
    assert response.status_code == 200
    assert response.json()['name'] == 'Pushok'
    yield response.json()['id']


def test_get_pet(test_create_pet):
    response = requests.get(f'{base_url}/{test_create_pet}')
    result = response.json()
    print()
    print('************************* CREATE ****************************')
    for key, value in result.items():
        print(f'{key}: {value}')
    assert response.status_code == 200


def test_put_pet(test_create_pet):
    put_id = test_create_pet
    payload = {
          "id": put_id,
          "category": {
            "id": 0,
            "name": "turtle"
          },
          "name": "Tortilla",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "green"
        }
    response = requests.put(base_url, json=payload)
    result = response.json()
    print()
    print('***************** PUT ************************')
    print(result)
    for key, value in result.items():
        print(f'{key}: {value}')
    checking = requests.get(f'{base_url}/{put_id}')
    print(checking.json())
    assert response.status_code == 200
    assert checking.json()['name'] == 'Tortilla'


def test_patch_pet():
    with open('pet_id.txt', 'r', encoding='utf-8') as f:
        pet_id = int(f.readline().strip())
    payload = {
          "id": pet_id,
          "category": {
            "id": 0,
            "name": "lion"
          },
          "name": "Simba",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
    response = requests.put(base_url, json=payload)
    result = response.json()
    print()
    print('******************** UPDATED *************************')
    for key, value in result.items():
        print(f'{key}: {value}')
    assert response.status_code == 200


def test_delete_pet(test_create_pet):
    response = requests.delete(f'{base_url}/{test_create_pet}')
    assert response.status_code == 200
    checking = requests.get(f'{base_url}/{test_create_pet}')
    print()
    print('*************** DELETE ********************')
    print(checking.json())
    assert checking.status_code == 404
    assert checking.json()['message'] == 'Pet not found'