from flask import Flask, jsonify, request

app = Flask(__name__)

# 🧾 Pre-added sample orders
orders = [
    {"item": "Chocolate Cake", "quantity": 2},
    {"item": "Red Velvet Cake", "quantity": 1},
    {"item": "Black Forest Cake", "quantity": 3}
]

@app.route('/')
def home():
    return "Order Service Running ✅"

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/add_order', methods=['GET'])
def add_order():
    item = request.args.get('item')
    quantity = request.args.get('quantity')
    if item and quantity:
        order = {'item': item, 'quantity': int(quantity)}
        orders.append(order)
        return jsonify({"message": "Order added successfully", "order": order}), 201
    else:
        return jsonify({"error": "Missing item or quantity"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
