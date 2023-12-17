from flask import Flask, request 
from Controllers import TaxContoller
from dotenv import load_dotenv
f
load_dotenv()
import os

SECRET_KEY = os.getenv("MY_SECRET")

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')


@app.route('/')
def index():
    return TaxContoller.test()


@app.route('/test', methods = ['POST'])
def test():
   return TaxContoller.jsontest(request)


@app.route('/tax', methods = ['POST'])
def taxt():
   return TaxContoller.taxcalc(request)



if __name__ == '__main__':
    app.run(debug=False)