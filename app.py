from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response("Hello world") #adds content
    response.status_code = 202
    response.headers['Git'] = 'Gud'
    return response

@app.route('/hello', methods=['GET', 'POST']) # u can specify the method by adding methods
def hello():
    if request.method == "GET":
        return "You made a get request", 223 # by adding a comma and a number u r making a response code
    return "helloski"

@app.route('/greet/<name>') # whats inside the <> plays the role of the parameter called URL processor
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>') # i can specify what kind of a value is getting passed by add for example int: which will turn it into a Integer
def add(number1, number2): # if passed something else than integer it gonna give me "not found" error
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/values') # handling url parameters for example /values?greeting=hello&name=Black
def values(): #its a great practice to check if the parameters are actually in URL
    if 'greetings' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting} {name}"
    else:
        return "some parameters are missing!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True) # debug is prefer before the uploading the application