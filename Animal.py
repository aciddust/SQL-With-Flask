import pymysql
from flask_restful import Resource
from Database import MySQL 

class AnimalIn(Resource):
    def __init__(self):
        self.db = MySQL().connect()
    def get(self):
        self.cursor = self.db.cursor()
        self.sql = 'SELECT * FROM ANIMAL_INS'
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.db.close()
        for r in self.rows:
            r['DATETIME'] = str(r['DATETIME'])
        
        return self.rows

class AnimalOut(Resource):
    def __init__(self):
        self.db = MySQL().connect()
    def get(self):
        self.cursor = self.db.cursor()
        self.sql = 'SELECT * FROM ANIMAL_OUTS'
        self.cursor.execute(self.sql)
        self.rows = self.cursor.fetchall()
        self.db.close()
        for r in self.rows:
            r['DATETIME'] = str(r['DATETIME'])
        
        return self.rows