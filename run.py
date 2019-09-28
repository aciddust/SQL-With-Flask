import os
import json
import pymysql
import datetime
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

load_dotenv()
db = pymysql.connect(host=os.getenv('MYSQL_HOST'),
                    port=int(os.getenv('MYSQL_PORT')),
                    user=os.getenv('MYSQL_USER'),
                    passwd=os.getenv('MYSQL_PASSWORD'),
                    db=os.getenv('MYSQL_DATABASE'),
                    charset=os.getenv('MYSQL_CHARSET'),
                    cursorclass=pymysql.cursors.DictCursor)

def json_default(value):
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')
    raise TypeError('not JSON serializable')


class Animal(Resource):
    def post(self):
        curs = db.cursor()
        sql = 'SELECT * FROM ANIMAL_INS'
        curs.execute(sql)
        rows = curs.fetchall()

        print(rows[1])
        return {'data':'hello'}

api.add_resource(Animal, '/animal')

@app.route('/animal/in')
def animal_in():
    curs = db.cursor()
    sql = 'SELECT * FROM ANIMAL_INS'
    curs.execute(sql)
    results = curs.fetchall()
    print(results)
    return render_template('animal_in.html', results=results)

@app.route('/animal/out')
def animal_out():
    curs = db.cursor()
    sql = 'SELECT * FROM ANIMAL_OUTS'
    curs.execute(sql)
    results = curs.fetchall()
    return render_template('animal_out.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

