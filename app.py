
from flask import Flask
from flask import jsonify

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "product list"})

@app.route('/products/<string:product_name>')
def getProduct():
    return jsonify({""})

if __name__ == '__main__':
    app.run(debug=True, port=4000);