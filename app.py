from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('home.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


app.secret_key = 'development key'


# @app.route('/home', methods=['POST', 'GET'])
# def thankyou():
#     form = request.form
#     emailfrom = form['email']
#     subject = form['subject']
#     message = form['message']
#     msg = Message(subject, sender=emailfrom, recipients=['me@jenkarla.com'])
#     mail.send(msg, message)
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
