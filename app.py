from flask import Flask, render_template, url_for, request, redirect
import csv
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_wiriter = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_wiriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

        if request.method == 'POST':
            form = request.form
            emailto = form['email']
            subject = form['subject']
            msg = Message(subject, sender=[emailto], recipients="me@jenkarla.com")
            Mail.send(msg)
        return render_template('/contact.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)

