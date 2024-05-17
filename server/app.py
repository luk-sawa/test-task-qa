from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from random import randint
from time import sleep
from order import Order


app = Flask(__name__)


orders = []


@app.route('/orders', methods=['GET', 'POST'])
def route_orders():
    random_delay()
    if request.method == 'GET':
        return jsonify([to_dict(order) for order in orders]), 200

    if request.method == 'POST':
        try:
            new_order = request.get_json()
        except BadRequest:
            return jsonify(error_response(400, 'Invalid input')), 400
        new_order = to_order(new_order)
        orders.append(new_order)
        response = to_dict(new_order)
        response['orderID'] = new_order.orderID
        return jsonify(response), 201


@app.route('/orders/<order_id>', methods=['GET', 'DELETE'])
def route_order_by_id(order_id):
    random_delay()
    if request.method == 'GET':
        order = find_order(order_id)
        response = to_dict(order)
        response['status'] = order.status
        return jsonify(response), 200

    if request.method == 'DELETE':
        order = find_order(order_id)
        orders.remove(order)
        return 'Order canceled', 204


def to_order(json_message):
    order = Order(json_message['stoks'], json_message['quantity'])
    return order


def to_dict(order):
    order_json = {'stoks': order.stocks, 'quantity': order.quantity}
    return order_json


def find_order(order_id):
    searched_order = next((order for order in orders if str(order.orderID) == order_id), None)
    if searched_order is None:
        return jsonify(error_response(404, 'Order not found')), 404
    return searched_order


def error_response(error_code, error_message):
    error = {
            'code': error_code,
            'message': error_message
        }
    return error


def random_delay():
    sleep(randint(100, 1000)/1000)
