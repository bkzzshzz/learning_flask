from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/hello')
# def hello():
#     return 'Hello!'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath {escape(subpath)}'

# #Unique URLS

# @app.route('/projects/') #like a folder
# def projects():
#     return 'The project page'

# @app.route('/about') #returns the html file
# def about():
#     return 'The about page'

#URL Building
# have to do from flask import url_for

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

#HTTP Methods

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# with app.test_request_context():
#     print(url_for('static', filename= 'style.css'))

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name = None):
#     return render_template ('hello.html', name=name)

#Accessing Request Data
#context locals

# from flask import request

with app.test_request_context('/hello', method = 'POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

searchword = request.args.get('key', '')



if __name__ == "__main__":
    app.run(debug=True)


    