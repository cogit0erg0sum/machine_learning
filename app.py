from flask import Flask
import sys
from housing.logger import logging


app = Flask(__name__)

@app.route("/", methods =['GET' , 'POST'])
def index():
    logging.info("checking logging file configpython a")
    return 'Starting my first ever ML Project. So Excited!!! CI-CD pipeline established'

if __name__ == "__main__":
    app.run(debug = True)