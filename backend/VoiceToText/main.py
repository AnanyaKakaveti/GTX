
from flask import Flask, jsonify, request, send_file
from flask_behind_proxy import FlaskBehindProxy
from InputAndCompare import *


app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '626423b656a4f6851a5cbece30f78108'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)


# Replace 'YOUR_API_KEY' with your actual API key
# api_key = 'YOUR_API_KEY'



#@app.route('/api', methods=['GET'])
#def hello1():
#    return jsonify({'message': 'Hello, this is your REST API!'})

@app.route('/', methods=['GET'])
def landing():
    return jsonify({'message': "Hello! the commands we have are!"})


@app.route('/api/record_without_translate', methods = ['GET'])
def rec():
    MakeUserFile()

@app.route('/api/get_user_input', methods=['GET'])
def hello(trueLine):
    if request.method == 'GET':
        trueLine = request.get('data')
        answer = GetUserInput(trueLine)
        return jsonify({'message': answer})

if __name__ == "__main__":
    app.run()