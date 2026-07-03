from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Black'
    myresult = 10 + 20
    mylist = {10, 20, 30, 40, 50, 60}
    return render_template('index.html', myvalue=myvalue, myresult=myresult, mylist=mylist) # adding foreign values outside the page

@app.route('/filter')
def other():
    someText = 'Hello world'
    return render_template('other.html', someText=someText)

@app.route('redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))


@app.route('/hello', methods=['GET', 'POST']) # u can specify the method by adding methods
def hello():
    if request.method == "GET":
        return "You made a get request", 223 # by adding a comma and a number u r making a response code
    response = make_response("Hello world") #adds content
    response.status_code = 202
    response.headers['Git'] = 'Gud'
    return "helloski"

@app.route('/greet/<name>') # whats inside the <> plays the role of the parameter called URL processor
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>') # i can specify what kind of a value is getting passed by add for example int: which will turn it into a Integer
def add(number1, number2): # if passed something else than integer it gonna give me "not found" error
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/values') # handling url parameters for example /values?greeting=hello&name=Black
def values(): #its a great practice to check if the parameters are actually in URL
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting} {name}"
    else:
        return "some parameters are missing!"


# you can add a custom filter to jinja
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True) # debug is prefer before the uploading the application