from flask import Flask, render_template, request, redirect, session
from docx import Document
import sqlite3

def tmp_f(date):
    fetch_new_orderlist(date, 'company')

def fetch_data():
    conn = sqlite3.connect('material_company.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM material')
    material = cur.fetchall()
    cur.execute('SELECT * FROM company')
    company = cur.fetchall()
    cur.execute('SELECT * FROM blueprint')
    blueprint = cur.fetchall()
    cur.execute('SELECT * FROM orderlist')
    orderlist = cur.fetchall()
    conn.close()
    return material, company, blueprint, orderlist

def fetch_product():
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    cursor.execute('''
                    SELECT mid, bid, mName, description, price
                    from material''')
    product = cursor.fetchall()
    connect.close()
    return product

def fetch_search_product(category, keyword):
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    
    if category == '0':  # mid
        cursor.execute('''
            SELECT mid, bid, mName, description, price
            FROM material
            WHERE mid LIKE ?;''', ('%' + keyword + '%',))
        
    elif category == '1':  # bid
        cursor.execute('''
            SELECT mid, bid, mName, description, price
            FROM material
            WHERE bid LIKE ?;''', ('%' + keyword + '%',))
        
    elif category == '2':  # mName
        cursor.execute('''
            SELECT mid, bid, mName, description, price
            FROM material
            WHERE mName LIKE ?;''', ('%' + keyword + '%',))
    product = cursor.fetchall()
    connect.close()
    return product
        
def fetch_search_material(blueprint_id):
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    cursor.execute('''
                    select DISTINCT material.mid, blueprint.bName, material.mname, material.description, material.price
                    from material, blueprint
                    where material.bid = blueprint.bid and blueprint.bid = ?''', (blueprint_id))
    
    product = cursor.fetchall()
    connect.close()
    return product

def fetch_new_orderlist(odate, cName):
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    cursor.execute('''
                    insert into orderlist (odate, cName) 
                    values (?, ?)''', (odate, cName))
    connect.commit()
    connect.close()

def fetch_search_orderlist(category, keyword):
    connect = sqlite3.connect('material_company.db')
    cursor = connect.cursor()
    
    if category == '0':  # mid
        cursor.execute('''
            SELECT oid, odate, cName
            FROM orderlist
            WHERE oid LIKE ?;''', ('%' + keyword + '%',))
        
    elif category == '1':  # bid
        cursor.execute('''
            SELECT oid, odate, cName
            FROM orderlist
            WHERE odate LIKE ?;''', ('%' + keyword + '%',))
        
    elif category == '2':  # mName
        cursor.execute('''
            SELECT oid, odate, cName
            FROM orderlist
            WHERE cName LIKE ?;''', ('%' + keyword + '%',))
    orderlist = cursor.fetchall()
    connect.close()
    return orderlist

material, company, blueprint, orderlist = fetch_data()
product_data = fetch_product()
app = Flask(__name__)
app.secret_key = 'my_key'

@app.route('/')
@app.route('/main/')
def main():
    return render_template('main.html')

@app.route('/main/product/', methods=['GET', 'POST'])
def product():
    filter_data = product_data
    if request.method == 'POST':
        keyword = request.form['keyword']
        category = request.form['category']
        filter_data = fetch_search_product(category, keyword) or []
    return render_template('product.html', item = filter_data)

@app.route('/main/order_form/')
def order_foam():
    return render_template('order_form.html')

@app.route('/main/order_form/write/', methods=['GET', 'POST'])
def write():
    filter_blueprint = blueprint
    item = []
    if request.method == 'POST':
        action = request.form.get('action')
        print(action)
        if action == 'select':
            date = request.form['date']
            company_name = request.form.get('company')
            blueprint_id = request.form.get('blueprint')
            session['date'] = date
            session['company_name'] = company_name
            session['blueprint_id'] = blueprint_id
            item = fetch_search_material(blueprint_id) or []
            print(date, company_name, blueprint_id)
        elif action == 'submit_order':
            date = session.get('date')
            company_name = session.get('company_name')
            blueprint_id = session.get('blueprint_id')
            quantities = {key: value for key, value in request.form.items() if key.startswith('6')}
            print(date, company_name, blueprint_id, quantities)
            print(type(date))
            tmp_f(date)


    return render_template('write_order_form.html', company=company, blueprint=filter_blueprint, item=item)


@app.route('/main/order_form/load/', methods=['GET', 'POST'])
def load():
    filter_list = orderlist
    if request.method == 'POST':
        keyword = request.form['keyword']
        category = request.form['category']
        filter_list = fetch_search_orderlist(category, keyword) or []
    return render_template('load_order_form.html', orderlist = filter_list)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
