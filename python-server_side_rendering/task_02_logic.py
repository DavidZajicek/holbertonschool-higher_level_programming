from flask import Flask, render_template
import json

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


@app.context_processor
def inject_items():
    with open('items.json') as file:
        _items: dict = json.loads(file.read())
        file.close()
    return dict(items=_items.get('items', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
