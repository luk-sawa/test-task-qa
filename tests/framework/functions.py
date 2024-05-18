import requests


def cleanup_order(order_id):
    requests.delete(f'http://127.0.0.1:5000/orders/{order_id}')