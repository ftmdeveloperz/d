# High Tech Form

from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    send_email(name, email, message)
    return 'Form submitted successfully!'

def send_email(name, email, message):
    msg = MIMEText(f'Name: {name}\nEmail: {email}\nMessage: {message}')
    msg['Subject'] = 'New Form Submission'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'funtoonsmultimedia@gmail.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
  
