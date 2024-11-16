from flask import Flask, render_template, request, redirect
import sqlite3

tmp_material = {}
tmp_material = [
    {
        'material_number': i,
        'blueprint_number': i,
        'material_name': 'new_material',
        'note': '협의',
        'quantity': 0,
        'price': 0,
    } for i in range(1, 11)
]

tmp_company = {}
tmp_company = [
    {
        'company_number': i,
        'company_name': 'new_company',
        'company_address': 'new_address',
        'company_phone': '010-1234-5678',
        'company_email': 'new_email',
    } for i in range(1, 11)
]

app = Flask(__name__)

@app.route('/')
@app.route('/main/')
def main():
    return render_template('main.html')

@app.route('/main/product/')
def product():
    return render_template('product.html', item = tmp_material)

@app.route('/main/order_form/')
def order_foam():
    return render_template('order_form.html')

@app.route('/main/order_form/write/')
def write():
    return render_template('write_order_form.html')

@app.route('/main/order_form/load/')
def load():
    return render_template('load_order_form.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)