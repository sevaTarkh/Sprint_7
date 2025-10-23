import requests
import allure
import sys
from datetime import datetime
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.data import Constants

class TestCreateCourier:
    

    @allure.title('Создаю курьера')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_courier_login_password_response_status_code_201(self, delete_curier):

        login_pass = [f"seva{datetime.now().strftime("%m%d%H%M%S%f")}", "1234"]
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier", data=payload)
        assert response.status_code == 201 and response.json()['ok'] == True

        delete_curier(login_pass[0], login_pass[1])

    @allure.title('Создаю пользователя с логином, который уже есть')
    @allure.description('Отправляем POST запрос с сущесвтующим логином, проверяем текст ошибки и статус ответа')
    def test_create_existing_courier_login_correct_message_text(self, create_curier_and_delete_after):

        login_pass = create_curier_and_delete_after

        payload = {
            "login": login_pass[0],
            "password": "1234"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier", data=payload)

        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.' and response.status_code == 409

    @allure.title('Создаю курьера, передаю в ручку не все обязательные поля')
    @allure.description('Отправляем POST запрос без обязательного поля, проверяем текст ошибки и статус ответа')
    def test_create_courier_login_correct_message_text(self):

        payload = {
            "login": "seva888"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier", data=payload)

        assert response.json()['message'] == "Недостаточно данных для создания учетной записи" and response.status_code == 400
