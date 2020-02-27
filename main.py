import os
from flask import *



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return {"status":"sucess"}


if __name__ == '__main__':
    app.run(host="0.0.0.0")
