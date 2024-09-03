import pytest
import requests
import time

#Base url of API

Base_url = "https://reqres.in/api"

def test_get_user_page():
    """Test GET request for user page 2."""
    url = f"{Base_url}/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["page"] == 2


def test_post_create_user():
    """Test post request to create user"""
    url = f"{Base_url}/users"
    payload = {
        "name": "Bhushan",
        "job": "QA"
    }
    response = requests.post(url,json=payload)
    assert response.status_code==201
    response_data=response.json()
    assert response_data ["name"]=="Bhushan"
    assert response_data ["job"]=="QA"

def test_Put_update_user():
    """test Put request """
    url = f"{Base_url}/users/2"
    payload={
        "name": "Sagar",
        "job": "Developer"
    }
    response= requests.put(url,json=payload)
    assert response.status_code==200
    response_data=response.json()
    assert response_data["name"]=="Sagar"
    assert response_data ["job"]== "Developer"

def test_post_register_user():
    """test for register user"""
    url= f"{Base_url}/register"
    payload={
        "email": "abc@gmail.com",
         "password": "bhushan"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert "token" in response_data

def test_get_user_with_delay():
    """Test get request for user delay """
    url = f"{Base_url}/users?delay=3"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["page"] == 1



def test_api_load(url, num_requests):
    response_times = []
    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_times.append(end_time - start_time)
        print(f"Request took: {end_time - start_time} seconds")

    return response_times

url = 'https://reqres.in/api/users?page=2'
num_requests = 100
response_times = test_api_load(url, num_requests)



