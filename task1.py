from flask import Flask
from flask import render_template
import smtplib


app = Flask(__name__)


@app.route('/contact-us.html/')
@app.route('/contact-us.html/<name>')
def contact_us_html(name=None):
    return render_template('contact-us.html',name=name)

@app.route('/send-email/')
def send_email():
    s = smtplib.SMTP('smtp.gmail.com',587)
    sender_email_id = 'masandelifechoices@gmail.com'
    receiver_email_id = 'gontyelenimasande@gmail.com'
    password = input('enter sender email password')

    s.starttls()

    s.login(sender_email_id,password)

    message = ' '

    s.send_message(sender_email_id,receiver_email_id,message)

    s.quit()
