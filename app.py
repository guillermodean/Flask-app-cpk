
from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

from products import products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/templates/graficas')
def graficas():
    return render_template('graficas.html')

@app.route('/templates/tablas')
def tablas():
    return render_template('tabla.html')

#PARA LANZAR LOS USUARIOS Y LAS CONEXIONES

# @app.route('/ping')
# def ping():
#     return jsonify({"message": "pong"})

# @app.route('/products')
# def getProducts():
#     return jsonify({"products": products, "message": "product list"})

# @app.route('/products/<string:product_name>')
# def getProduct():
#     return jsonify({""})

if __name__ == '__main__':
    app.run(debug=True, port=4000) #debug true lo que hace es que cada vez que cambie algo se reinicia