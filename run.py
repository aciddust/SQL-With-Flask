from flask import Flask, render_template
from flask_restful import Resource, Api
from Database import MySQL
from Animal import AnimalIn, AnimalOut

app = Flask(__name__)
api = Api(app)

api.add_resource(AnimalIn, '/api/animal/in')
api.add_resource(AnimalOut, '/api/animal/out')

@app.route('/animal/in')
def animal_in():
    db = MySQL().connect()
    cursor = db.cursor()
    sql = 'SELECT * FROM ANIMAL_INS'
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('animal_in.html', results=results)

@app.route('/animal/out')
def animal_out():
    db = MySQL().connect()
    cursor = db.cursor()
    sql = 'SELECT * FROM ANIMAL_OUTS'
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('animal_out.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

