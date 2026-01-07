from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Sanjay' and password== '123':
            return "Success"
        else:
            return "failure"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)