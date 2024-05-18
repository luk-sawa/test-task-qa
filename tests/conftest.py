import pytest
import requests
from .framework.data import orders_list, single_order
from .framework.functions import cleanup_order


@pytest.fixture
def fill_database_with_orders():
    responses = []
    order_ids = []
    orders = orders_list()
    for body in orders:
        response_json = requests.post('http://127.0.0.1:5000/orders', json=body).json()
        responses.append(response_json)
        order_ids.append(response_json['orderID'])
    yield responses
    for order_id in order_ids:
        cleanup_order(order_id)


@pytest.fixture
def prepare_order():
    json_body = single_order()
    response_json = requests.post('http://127.0.0.1:5000/orders', json=json_body).json()
    order_id = response_json['orderID']
    yield response_json
    cleanup_order(order_id)
