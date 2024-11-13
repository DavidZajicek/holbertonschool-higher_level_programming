from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    return render_template('items.html')


@app.route('/products')
def products():
    return render_template('product_display.html')


@app.context_processor
def inject_items():
    with open('items.json') as file:
        _items: dict = json.loads(file.read())
        file.close()

    def get_products():
        _products = []
        if request.args.get('source') == "json" or request.args.get('source') == "csv":
            if request.args.get('source') == "json":
                with open('products.json') as products_f:
                    _products = json.loads(products_f.read())
                    products_f.close()
            if request.args.get('source') == "csv":
                with open('products.csv') as products_f:
                    _products_reader = csv.DictReader(products_f)
                    for row in _products_reader:
                        _products.append(row)
                    products_f.close()
            if request.args.get('id'):
                print(_products)
                single_product = [x for x in _products if str(x['id']) == request.args.get('id')]
                if single_product:
                    return single_product
                else:
                    return "ID not found"
            return _products
        else:
            return "invalid-source"

    return dict(items=_items.get('items', []), products=get_products())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
