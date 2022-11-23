from flask_mail import Mail, Message

mail = Mail()

def send_email(recipent, mail=mail):

   return "Success"

   msg = Message('Hello', sender = ('Eyadaty ', 'info@eyadaty.com'), recipients = [recipent])
   msg.body = ("This is the email body")
   msg.subject = "Welcome to Eyadaty"
   mail.send(msg)
   return "Success"