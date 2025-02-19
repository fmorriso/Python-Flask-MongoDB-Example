import sys
from flask import Flask, jsonify, Blueprint, app

from pymongo import MongoClient

from program_settings import ProgramSettings


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

def get_connection_string() -> str:
    """
    Get a connection string for MongoDB using the key/values stored in the .env file.
    :return: a string containing the connection string.
    """
    template: str = ProgramSettings.get_setting('MONGODB_CONNECTION_TEMPLATE')
    uid: str = ProgramSettings.get_setting('MONGODB_UID')
    pwd: str = ProgramSettings.get_setting('MONGODB_PWD')

    conn_string = f'mongodb+srv://{uid}:{pwd}@{template}'
    print(f'{conn_string=}')
    return conn_string

def get_mongodb_client() -> MongoClient:
    """get a client connection to my personal MongoDB Atlas cluster using my personal usrid and password"""
    connection_string: str = get_connection_string()
    connection: MongoClient = MongoClient(connection_string)
    return connection


bp = Blueprint('main', __name__)
# Connect to MongoDB



@bp.route('/')
def hello_world():  # put application's code here
    return f'Hello World using Python {get_python_version()}'

"""
FIX THIS METHOD
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]
@bp.route('/users', methods = ['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)
"""

@bp.route('/about')
def about():
    return f"About Page: {get_connection_string()}"
