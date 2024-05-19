import requests
from .data import url_address


def cleanup_order(order_id):
    requests.delete(f'{url_address()}/orders/{order_id}')