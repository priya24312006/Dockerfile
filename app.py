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



from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

# Initialize DB and add default products
with app.app_context():
    db.create_all()
    
    # Add default products only if DB is empty
    if Product.query.count() == 0:
        default_products = [
            {"name": "Chocolate Cake", "price": 499},
            {"name": "Vanilla Cupcake", "price": 99},
            {"name": "Strawberry Tart", "price": 299},
            {"name": "Blueberry Muffin", "price": 149},
            {"name": "Red Velvet Cake", "price": 599},
            {"name": "Lemon Pie", "price": 349},
            {"name": "Carrot Cake", "price": 399},
            {"name": "Chocolate Brownie", "price": 199},
            {"name": "Pineapple Cake", "price": 449},
            {"name": "Coffee Muffin", "price": 129},
            {"name": "Mango Tart", "price": 279},
            {"name": "Black Forest Cake", "price": 699}
        ]
        for prod in default_products:
            db.session.add(Product(name=prod["name"], price=prod["price"]))
        db.session.commit()

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    p = Product.query.get(product_id)
    if p:
        return jsonify({"id": p.id, "name": p.name, "price": p.price})
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    p = Product(name=data['name'], price=data['price'])
    db.session.add(p)
    db.session.commit()
    return jsonify({"message": "Product added", "id": p.id})

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    p = Product.query.get(product_id)
    if not p:
        return jsonify({"error": "Product not found"}), 404
    data = request.json
    p.name = data.get('name', p.name)
    p.price = data.get('price', p.price)
    db.session.commit()
    return jsonify({"message": "Product updated"})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    p = Product.query.get(product_id)
    if not p:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(p)
    db.session.commit()
    return jsonify({"message": "Product deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)




from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Priyanka", "email": "priyanka@example.com"},
    {"id": 2, "name": "Advik", "email": "advik@example.com"}
]

@app.route('/')
def home():
    return "User Service is running successfully 🚀"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = {"id": len(users) + 1, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)



