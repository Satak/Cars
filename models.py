
from peewee import *

db = SqliteDatabase('mydb.db')

class Car(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()

    class Meta:
        database = db

def init_db():
    db.connect()
    db.create_tables([Car], safe=True)
