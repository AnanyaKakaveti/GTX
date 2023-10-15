
from flask import Flask, jsonify, request, send_file, Response
#from flask_behind_proxy import FlaskBehindProxy
from InputAndCompare import *


app = Flask(__name__)
#proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '626423b656a4f6851a5cbece30f78108'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String)


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



@app.route('/video_feed')
def video_feed():
    return Response(DisplayThroughCV(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__": 
    #app.run(host = '127.0.0.1', port = 5000)
    app.run()