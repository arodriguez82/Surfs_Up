from flask import Flask

# Create an instance
app = Flask(__name__)

# Create an app route ('/') denotes putting the data at the root of the route - highest heirarchy of data
@app.route('/')
def hello_world():
    return 'Hello World!'