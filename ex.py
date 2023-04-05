from flask import flask
app=Flask(__name__)

@app.route('/')

def index():
    return "Hello World! from Flask"
    
if__name__="__main":
    app.run(debug=True)
