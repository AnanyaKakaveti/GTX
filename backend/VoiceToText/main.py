
from flask import Flask, jsonify, request, send_file,render_template,send_file
from InputAndCompare import *
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': "Reached Server!"})

#Test Function

@app.route('/api/record_without_translate', methods = ['GET'])
def rec():
    MakeUserFile()

#Test the record function

@app.route('/api/get_user_input/<trueLine>', methods=['GET'])  
def hello(trueLine):      
    #type out {numbers}/api/get_user_input
    answer = GetUserInput(trueLine)
    print(f"trueLine: {trueLine}")
    return jsonify({'message': answer})



#This file will upload a mp4 file to the server. 
# This will be neccesary for automatomation 
@app.route('/h_video/<name>')          #plan to implement version with automation
def video_feed(name):
    
    directory_path = os.path.join(os.getcwd(), "backend", "VoiceToText", name)
    onlyInProject = f"\\backend\VoiceToText\\" +  name
    return send_file(directory_path, as_attachment=True)
    print(directory_path)
    

if __name__ == "__main__": 
    #app.run(host = '127.0.0.1', port = 5000)
    app.run()