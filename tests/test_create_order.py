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
    @pytest.mark.parametrize('payload', [
        Constants.order_black,
        Constants.order_grey,
        Constants.order_brack_grey,
        Constants.order_without_colors
    ])
    def test_create_order_code_201(self, payload):

        payload = json.dumps(payload)

        response = requests.post(f"{Constants.url_samokat}/api/v1/orders", data=payload)

        assert response.status_code == 201 and 'track' in response.json()