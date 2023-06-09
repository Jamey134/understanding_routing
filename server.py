from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat_word(num, word):
#     print(num * word)

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    return(num * name)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
