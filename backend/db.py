# https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb
import datetime
import bson

from flask import current_app, g
from flask_pymongo import PyMongo

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId

client = MongoClient('mongodb+srv://sbuhacks:sbuhacks123@cluster0.jkkkjsb.mongodb.net/?retryWrites=true&w=majority')
db = client.notely

# create
def create_user() -> ObjectId:
    try:
        print('database is ', db.notely.users)
        result = db.users.insert_one({
            'summaries': [], 
            # 'created_at': datetime.datetime.now()
        })
        return result.inserted_id
    except Exception as e:
        return e

def create_summary(title : str, text_content : str) -> ObjectId:
    try:
        result = db.summaries.insert_one({
            'title': title, 
            'text_content': text_content, 
            # 'created_at': datetime.datetime.now()
        })
        return result.inserted_id
    except Exception as e:
        print(e)
        return e

# get individual
def get_user(user_id : ObjectId) -> object:
    try:
        return list(db.users.find_one({'_id' : user_id}))
    except Exception as e:
        return e

def get_summary(summary_id : ObjectId) -> object:
    try:
        return db.summaries.find_one({'_id' : summary_id})
    except Exception as e:
        return e

# get summaries
def get_summaries() -> list:
    try:
        return list(db.summaries.find({}))
    except Exception as e:
        return e
    