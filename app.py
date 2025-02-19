import sys
from routes import bp
from flask import Flask, jsonify
from pymongo import MongoClient

from program_settings import ProgramSettings

app = Flask(__name__)
# route information is in a separate file, so use Blueprint feature of Flask
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug = True)
