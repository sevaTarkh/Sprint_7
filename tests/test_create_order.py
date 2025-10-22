import requests
import allure
import sys
import os
import pytest
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.data import Constants


class TestCreateOrder:

    
    @allure.title('Создаю заказ')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    @pytest.mark.parametrize('payload', [{
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK",
                "GREY"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
        }
    ])
    def test_create_order_code_201(self, payload):

        payload = json.dumps(payload)

        response = requests.post(f"{Constants.url_samokat}/api/v1/orders", data=payload)

        assert response.status_code == 201 and 'track' in response.json()