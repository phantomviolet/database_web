from flask import Flask, render_template, request, redirect
from docx import Document
import sqlite3

def fetch_data():
    conn = sqlite3.connect('material_company.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM material')
    material = cur.fetchall()
    cur.execute('SELECT * FROM company')
    company = cur.fetchall()
    conn.close()
    return material, company

def fetch_product():
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    cursor.execute('''SELECT need.mid, bid, material.mName, description, price
                    from need, material
                    where need.mid = material.mid;''')
    product = cursor.fetchall()
    connect.close()
    return product


material, company = fetch_data()
product_data = fetch_product()
print(product_data)
app = Flask(__name__)

@app.route('/')
@app.route('/main/')
def main():
    return render_template('main.html')

@app.route('/main/product/')
def product():
    return render_template('product.html', item = product_data)

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