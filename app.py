
"""main app"""
from flask import Flask, render_template, request, redirect, url_for, send_file
from models import *

app = Flask(__name__, static_folder='client')

@app.before_request
def before_request():
    init_db()

@app.teardown_request
def teardown_request(e):
    db.close()

@app.route('/cars')
def cars():
    return render_template('index.html')

# UI Route
@app.route('/<int:carid>')
@app.route('/')
def home(carid=None):
    if carid:
        cars = Car.select().where(Car.id == carid)
        template = 'edit.html'
        if not cars:
            template = 'home.html'
    else:
        cars = Car.select()
        template = 'home.html'

    return render_template(template, car=cars)

# POST Car
@app.route('/new/car', methods=['POST'])
def new_car():
    try:
        res = Car.create(
            make=request.form['Make'],
            model=request.form['Model'],
            year=request.form['Year']
        )
    except Exception as error:
        pass
    return redirect(url_for('home'))

# DELETE Car
@app.route('/delete/car/<int:carid>', methods=['POST'])
def delete_car(carid):
    car = Car.get(Car.id == carid)
    if car:
        car.delete_instance()

    return redirect(url_for('home'))

# PUT Car
@app.route('/update/car/<int:carid>', methods=['POST'])
def update_car(carid):
    try:
        car = Car.get(Car.id == carid)
        if car:
            car.make = request.form['Make']
            car.model = request.form['Model']
            car.year = request.form['Year']

            car.save()
    except Exception as error:
        pass
    return redirect(url_for('home'))

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
