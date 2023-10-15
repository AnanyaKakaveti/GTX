
from flask import Flask, jsonify, request, send_file
from InputAndCompare import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for your app

@app.route('/', methods=['GET'])
def landing():
    return jsonify({'message': "Hello! the commands we have are!"})


@app.route('/api/record_without_translate', methods = ['GET'])
def rec():
    MakeUserFile()


@app.route('/api/get_user_input/<trueLine>', methods=['GET'])  
def hello(trueLine):      
    #type out {numbers}/api/get_user_input
    answer = GetUserInput(trueLine)
    print(f"trueLine: {trueLine}")
    return jsonify({'message': answer})


if __name__ == "__main__": 
    #app.run(host = '127.0.0.1', port = 5000)
    app.run()