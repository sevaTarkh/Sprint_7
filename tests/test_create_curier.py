import requests
import allure
import sys
import pytest
from datetime import datetime
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from helpers.CreateCurier import register_new_courier_and_return_login_password
from data.data import Constants

class TestCreateCourier:
    

    @allure.title('Создаю курьера')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_courier_login_password_response_status_code_201(self):

        payload = {
            "login": f"seva{datetime.now().strftime("%m%d%H%M%S%f")}",
            "password": "1234"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier", data=payload)
        assert response.status_code == 201 and response.json()['ok'] == True

    @allure.title('Создаю пользователя с логином, который уже есть')
    @allure.description('Отправляем POST запрос с сущесвтующим логином, проверяем текст ошибки и статус ответа')
    def test_create_existing_courier_login_correct_message_text(self):

        login_pass = register_new_courier_and_return_login_password()

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
