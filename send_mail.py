import os
import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = os.getenv('SMTP_PORT')
    smtp_server = os.getenv('SMTP_SERVER')
    login = os.getenv('SMTP_USERNAME')
    password = os.getenv('SMTP_PASSWORD')
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'mailtrap@demomailtrap.com'
    receiver_email = 'bingwanan@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
