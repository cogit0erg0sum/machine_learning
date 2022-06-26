from flask import Flask
import sys


app = Flask(__name__)

@app.route("/", methods =['GET' , 'POST'])
def index():
    return 'Starting my first ever ML Project. So Excited!!! CI-CD pipeline established'

if __name__ == "__main__":
    app.run(debug = True)