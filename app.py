from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/", methods =['GET' , 'POST'])
def index():
    logging.info("We are testing logging module")
    return 'Starting my first ever ML Project. So Excited!!! CI-CD pipeline established'

if __name__ == "__main__":
    app.run(debug = True)