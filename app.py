from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods =['GET' , 'POST'])
def index():
    try:
        raise Exception("Trying to raise excepton")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return 'Starting my first ever ML Project. So Excited!!! CI-CD pipeline established'

if __name__ == "__main__":
    
    app.run(debug = True)