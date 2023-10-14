
from flask import Flask, jsonify, request, send_file
from InputAndCompare import *
app = Flask(__name__)


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


@app.route('/api/get_user_input/<int:trueLine>', methods=['GET'])      #type out {numbers}/api/get_user_input
def hello(trueLine):
    answer = GetUserInput(trueLine)
    return jsonify({'message': answer})


"""def chatGptResponse(question):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
    return response['choices'][0]['message']['content']
    """

if __name__ == "__main__":
    app.run()