from flask import Flask, jsonify, request, send_file
from InputAndCompare import GetUserInput
app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
# api_key = 'YOUR_API_KEY'



#@app.route('/api', methods=['GET'])
#def hello1():
#    return jsonify({'message': 'Hello, this is your REST API!'})
print(GetUserInput())

@app.route('/api/get_user_input', methods=['GET'])
def hello():
    answer = GetUserInput()
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