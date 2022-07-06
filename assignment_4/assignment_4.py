from flask import render_template, redirect, Blueprint
from flask import request
import mysql.connector

assignment_4 = Blueprint('assignment_4', __name__, static_folder='static', template_folder='templates')


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


@assignment_4.route('/assignment_4')
def assignment_44():
    query = 'SELECT * FROM users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user_id = request.form['user_id']
    query = "INSERT INTO users(name,email,password,id) VALUES ('%s','%s','%s','%s')" % (name, email, password, user_id)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment_4')


@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    name = request.form['name']
    age = request.form['age']
    query = "UPDATE users SET age='%s' WHERE name='%s'" % (age, name)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment_4')


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s';" % name
    interact_db(query=query, query_type='commit')
    return redirect('/assignment_4')


@assignment_4.route('/assignment_4')
def assi_func():
    return render_template('assignment_4.html')
