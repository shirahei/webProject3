from flask import Flask
from flask import request, session
from flask import render_template

app = Flask(__name__)
app.secret_key='123'

@app.route('/')
def hello_world():
    # put application's code here
    return render_template('index.html',name='Ariel',second_name='Petch')

@app.route('/about')
def about_func():
    return render_template('about.html')

@app.route('/home')
def home_func():
    return render_template('home.html')

@app.route('/catalog')
def catalog_func():
    if 'id' in request.args:
        curr_id = request.args['id']
        name = request.args['name']
        return f'User Name:{name}, The Id of product:{curr_id}'
    return 'in Catalog'

@app.route('/example')
def example_func():
    username=""
    if request.method =='Post':
        #check if the DB of the website
        username = request.form['username']

    return render_template('example.html', request.method,username=username)

if __name__ == '__main__':
    app.run()
