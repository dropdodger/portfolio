from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         message = data['message']        
#         file = database.write(f'\n{name}, {email}, {message}')

# def write_to_csv(data):
#     with open('database.csv', newline='', mode='a') as database2:
#         name = data['name']
#         email = data['email']
#         message = data['message']        
#         csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([name, email, message])

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        writer = csv.DictWriter(database, fieldnames=data.keys())
        writer.writerow(data)
        database.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. try again!'