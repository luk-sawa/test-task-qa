from flask import Flask, request
import json


app = Flask(__name__)


orders = []


@app.route('/orders', methods=['GET', 'POST'])
def route_orders():
    if request.method == 'GET':
        return [order.to_json() for order in orders], 200

    if request.method == 'POST':
        try:
            json.loads(request.get_json())
        except ValueError:
            return "Invalid input", 400
        new_order = request.get_json()
        orders.append(new_order)
        return new_order, 201


@app.route('/orders/<order_id>', methods=['GET', 'DELETE'])
def route_order_by_id(order_id):
    if request.method == 'GET':
        try:
            orders[order_id]
        except ValueError:
            return 'Order not found', 404
        return orders[order_id].to_json(), 200

    if request.method == 'DELETE':
        try:
            orders[order_id]
        except ValueError:
            return 'Order not found', 404
        orders.pop(order_id)
        return 'Order canceled', 204
