from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"name":"Laptop", "Price": 50000, "Category":"Electronic"},
    {"name":"Mobile", "Price": 40000, "Category":"Electronic"},
    {"name":"TAB", "Price": 17000, "Category":"Electronic"},

]
@app.route('/product', methods = ['GET'])
def product_details():

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)