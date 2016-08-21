from flask import Flask

# use whatever your current namespace is.It is like saying always refer to yourself.
app = Flask(__name__)

# specifying a route
@app.route('/')
@app.route('/<name>')  # Allows app to get input from the user without having to use request
#  Tells flask to capture whatever comes after the forward slash as an argument name
def index(name="Troy"):
    return "Hey there, Its {} here".format(name)


@app.route('/add/<int:num1>/<int:num2>') # conversion of input into into num datatype within URL
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)
# debug helps flask autorestart everytime we make changes to our application.


app.run(debug=True, port=8000, host='0.0.0.0')