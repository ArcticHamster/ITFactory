from flask import Flask


app = Flask(__name__)

@app.route('/hello')

def hello_world():
    return 'This is my first Flask app!'

@app.route('/')

def home_page():
    return 'This is my home page'

if __name__ == '__main__':
    app.run()

@app.route('/hello/<name>')

def hello_name(name):
    return f'Hello {name}'

from flask import url_for, redirect

@app.route('/users/<int:user_id>')

def hello_user(user_id):
    users = {
        1: 'Adela',
        2: 'Ion',
        3: 'Maria',
        4: 'Gheo',
        5: 'Mihai'
    }
    if user_id in users:
        username = user_id[users]
        return redirect(url_for('hello name', name = username))
    else:
        return 'Not a valid user'
