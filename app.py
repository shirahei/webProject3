from flask import Flask
from flask import render_template, request, redirect, url_for
from datetime import timedelta
from flask import request, session, jsonify
from flask import session
import time
import requests
import mysql.connector

app = Flask(__name__)
app.secret_key = '147258'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)


@app.route('/contact')
def contact_func():
    return render_template("contact.html")


@app.route('/home')
def home_func():
    username = ''
    return render_template("home.html", username=username)


@app.route('/')
def home_route():
    return redirect(url_for('home_func'))


@app.route('/assignment3_1')
def assignment3_1():
    return render_template("assignment3_1.html",
                           hobbies=['Playing chess', 'Solving Puzzle Games', 'Reading Books and Articles',
                                    'Cooking and Baking', 'Traveling'])


users = {'Maryam': 'maryam72@hotmail.com',
         'Josiane': 'josiane.deckow@dietrich.biz',
         'Rosamond': 'rosamond.hyatt@kub.com',
         'Reva': 'reva.schmeler@hotmail.com',
         'Blanda': 'blanda.jules@moore.biz'}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    name = "jkjlk"
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['psw']
        session['name'] = name
    else:
        if 'search' in request.args:
            name = request.args['search']
            if name in users:
                return render_template('assignment3_2.html', name=name, email=users[name])
            elif name == '':
                return render_template("assignment3_2.html", users=users)
            else:
                return render_template('assignment3_2.html', message='Cant Find User')
    return render_template("assignment3_2.html")


users_password = {'Maryam': '27223',
                  'Josiane': 'jd343',
                  'Rosamond': '23313',
                  'Reva': '65464',
                  'Blanda': '11432'}


@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name in users_password:
            password_in_dict = users_password[name]
            if password_in_dict == password:
                return render_template('log_in.html', message=
                "Logged-in", name=name, email=users[name])
            else:
                return render_template('log_in.html', message=
                "Wrong Password")
        else:
            return render_template('log_in.html', message=
            "Please Sign up")
    return render_template('log_in.html')


@app.route('/user', methods=['GET', 'POST'])
def user_func():
    return render_template('user.html',
                           hobbies=['Playing chess', 'Solving Puzzle Games', 'Reading Books and Articles',
                                    'Cooking and Baking', 'Traveling'])


@app.route('/log_out')
def logout_func():
    session.clear()
    return render_template('assignment3_2.html')


@app.route('/session')
def session_func():
    return jsonify(dict(session))


@app.route('/google')
def redirect_to_link():
    return redirect('https://google.com')

## Assignment_4
from assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)

@app.route('/assignment_4/users')
def users_4():
    query = 'SELECT * FROM users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


@app.route('/assignment_4/restapi_users', defaults={'user_id': 1})
@app.route('/assignment_4/restapi_users/<int:user_id>')
def get_user(user_id):
    query = f'select * from users where id= {user_id}'
    users_list = interact_db(query, query_type='fetch')

    if len(users_list) == 0:
        return_dict = {
            'message': 'user not found'
        }
    else:
        user_list = users_list[0]
        return_dict = {'name': user_list.name,
                       'email': user_list.email
                       }
    return jsonify(return_dict)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statement.
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

if __name__ == '__main__':
    app.debug = True
    app.run()
