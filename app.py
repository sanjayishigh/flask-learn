from flask import Flask, request,make_response, redirect, url_for, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return "I am back"

@app.route('/hello', methods=['POST','GET'])
def hello():
    response = make_response('Hello World')
    response.status_code = 201
    response.headers['content-type'] = 'text/plain'
    
    return response

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/nums/<int:num1>/<int:num2>')
def nums(num1, num2):
    return f" {num1} + {num2} ={num1 + num2}"

@app.route('/handle_url_params')
def params():
    greeting = request.args['greeting']
    name = request.args.get('name')
    return f"{greeting} {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)