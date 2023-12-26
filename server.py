from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/<string:page_name>')
def get_page(page_name):
    return render_template(f'/pages/{page_name}')

def write_to_file(data):
    with open('./database.txt', mode='a') as db:
        db.write(f'\n{data["email"]},{data["subject"]},{data["message"]}')

def write_to_csv(data):
    with open('./db.csv', mode='a') as db2:
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if(request.method == 'POST'):
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/form-submitted.html')
        except:
            return 'do not save to database'
    else:
        return 'Something went wrong!'
