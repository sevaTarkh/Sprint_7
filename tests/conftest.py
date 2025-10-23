import pytest
import requests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from helpers.create_user import register_new_courier_and_return_login_password
from data.data import Constants


@pytest.fixture
def create_curier_and_delete_after():

    login_pass = register_new_courier_and_return_login_password()
    yield login_pass

    if login_pass:  
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        
        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)
        if response.status_code == 200:
            courier_id = response.json()['id']

            requests.delete(f"{Constants.url_samokat}/api/v1/courier/{courier_id}")

@pytest.fixture
def delete_curier():
    couriers_to_delete = []  
    
    def _register_courier(login, password):
        couriers_to_delete.append((login, password))
    
    yield _register_courier
    
    for login, password in couriers_to_delete:
        payload = {"login": login, "password": password}
        response = requests.post(f"{Constants.url_samokat}/api/v1/courier/login", data=payload)
        if response.status_code == 200:
            courier_id = response.json()['id']
            requests.delete(f"{Constants.url_samokat}/api/v1/courier/{courier_id}")



