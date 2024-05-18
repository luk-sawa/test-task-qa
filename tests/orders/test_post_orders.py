import pytest
import requests
from ..framework.data import single_order, incorrect_single_order
from ..framework.functions import cleanup_order


def test_post_orders():
    order = single_order()
    response = requests.post('http://127.0.0.1:5000/orders', json=order)
    response_json = response.json()
    assert response.status_code == 201
    assert response_json['stoks'] == order['stoks'] and response_json['quantity'] == order['quantity']
    assert response_json['orderID'] is not None
    cleanup_order(response_json['orderID'])


def test_post_wrong_orders():
    order = incorrect_single_order()
    response = requests.post('http://127.0.0.1:5000/orders', data=order)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json['code'] == 400 and response_json['message'] == 'Invalid input'


def test_post_different_mimetype_orders():
    order = single_order()
    response = requests.post('http://127.0.0.1:5000/orders', data=order)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json['code'] == 400 and response_json['message'] == 'Invalid input'
