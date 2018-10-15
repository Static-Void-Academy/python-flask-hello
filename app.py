from flask import Flask
from flask import request
app = Flask(__name__)

# Basic Route
@app.route("/")
def hello():
    return "Hello World!"

# Route with parameter in route
# Variable must be passed to method
@app.route("/test/<param>")
def param_test(param):
    return "Received: {}".format(param)

# Route with type constraint on parameter
@app.route("/test/square/<int:param>")
def int_test(param):
    return "Square of {} is {}".format(param, param * param)

# Route with parameters passed as args
# Example: /test/args?name=<name>&age=<age>
@app.route("/test/args")
def arg_test():
    name = request.args.get('name')
    age = request.args.get('age')
    return "Name is {}\nAge is {}".format(name, age)

# Route with HTTP method constraints
@app.route("/methods", methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        return "Received POST Request"
    else:
        return "Received GET Request"
