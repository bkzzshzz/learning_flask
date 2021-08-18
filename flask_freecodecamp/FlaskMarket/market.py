from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<b>Hello, World! Changed.</b>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
