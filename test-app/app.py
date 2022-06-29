import os
from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__) 

# configure flask_mail
app.config['MAIL_SERVER']=os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = os.environ.get("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = "True" == os.environ.get("MAIL_USE_TLS")
app.config['MAIL_USE_SSL'] = "True" == os.environ.get("MAIL_USE_SSL")

# init mail client
mail = Mail(app)

# send email to mail server
@app.route("/mail", methods=["post"])
def sendMail():
    if request.method != "POST":
        return "Error! Route only accepts POSTS!"
   
    raw_msg = request.form.get("message")
 
    msg = Message(raw_msg, sender = 'fake@email.com', recipients = ['fake@email.com'])
    msg.body = raw_msg
    mail.send(msg)
    return "Message sent!", 200

# simple index route with basic email form
@app.route("/")
def index():
    return '''<form action="/mail" method="post">
               <ul>
                 <li>
                    <label for="message">Message:</label>
                    <input type="text" id="message" name="message">
                 </li>
               </ul>
             </form>
            '''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
