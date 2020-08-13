from flask import Flask, render_template, url_for, request, redirect
import csv
from flask_mail import Mail, Message
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# set configuration and instantiate mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'jagadish.pasham@gmail.com',
    "MAIL_PASSWORD": 'ytdzhduheugrujco'
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/')
def my_home():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    if request.method == 'POST':
        form = request.form
        emailto = form['email']
        subject = form['subject']
        msg = Message(subject, sender=emailto, recipients=['me@jenkarla.com'])
        mail.send(msg)
    return redirect('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
