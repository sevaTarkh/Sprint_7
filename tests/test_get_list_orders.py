import requests
import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.data import Constants

class TestGetListOrders:
    

    @allure.title('Получаю спсиок заказов')
    @allure.description('Отправляем GET запрос, проверяем что возвращается не пустой список заказов')
    def test_get_orders_response_status_code_200(self):

        response = requests.get(f"{Constants.url_samokat}/api/v1/orders")
        assert response.status_code == 200 and response.json()['orders'] != []