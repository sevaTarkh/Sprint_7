import requests
import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants


class TestLoginCourier:


    @allure.title('Логин курьера')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_login_courier_login_password_response_status_code_200(self, create_curier_and_delete_after):


        login_pass = create_curier_and_delete_after
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)
        assert 'id' in response.json() and response.status_code == 200


    @allure.title('Авторизация курьера без логина')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ошибки')
    def test_login_courier_with_out_login_status_code_400(self):

        payload = {
            "password": "password"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)

        assert response.json()['message'] == "Недостаточно данных для входа" and response.status_code == 400


    # инфраструктурная проблема при отправке запроса без пароля, запрос падает с ошибкой 504
    @allure.title('Авторизация курьера без пароля')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ошибки')
    def test_login_courier_with_out_password_status_code_400(self):

        payload = {
            "login": "login_pass[0]"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)

        assert response.json()['message'] == "Недостаточно данных для входа" and response.status_code == 400

    @allure.title('Не правильный логин/пароль курьера')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ошибки')
    def test_login_courier_uncorrect_login_status_code_404(self):

        payload = {
            "login": "login_pass[0]",
            "password": "123123"
        }

        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)

        assert response.json()['message'] == "Учетная запись не найдена" and response.status_code == 404