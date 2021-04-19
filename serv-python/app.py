from flask import Flask, request, render_template, session, redirect
import requests

app = Flask(__name__)

#--------------------------------------------Home----------------------------------------#
@app.route('/', methods = ['GET'])
def home():
#----------Code-------------------#



if __name__ == "__main__":
    app.run(port=3030, host='0.0.0.0', debug=True)

