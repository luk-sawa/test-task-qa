import pytest
import requests
from ..framework.data import url_address


def test_get_orders_with_id(prepare_order):
    premade_order = prepare_order
    premade_order_id = premade_order['orderID']
    response = requests.get(f'{url_address()}/orders/{premade_order_id}')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['stoks'] == premade_order['stoks'] and response_json['quantity'] == premade_order['quantity']
    assert response_json['status'] is not None


def test_get_orders_with_incorrect_id(prepare_order):
    response = requests.get(f'{url_address()}/orders/123')
    response_json = response.json()
    assert response.status_code == 404
    assert response_json['code'] == 404 and response_json['message'] == 'Order not found'
