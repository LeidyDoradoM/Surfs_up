from flask import Flask

#create a new flask app instance
app = Flask(__name__)

#create the first route
@app.route('/')
def hello_world():
    return 'Hello world'
