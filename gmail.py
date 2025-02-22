import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:

    def __init__(self,To='jashwanthreddysungjin@gmail.com'):
        self.form="tangwulinggd@gmail.com"
        self.password='rzeg nfsi swsd brcz'
        self.to=To

    def sendMail(self,subject,body):
        message=MIMEMultipart()
        message['From']=self.form
        message['To']=self.to
        message['Subject']=subject

        message.attach(MIMEText(body,'plain'))

        try:
            with smtplib.SMTP("smpt.gmail.com",587) as server:
                server.starttls()
                server.login(self.form,self.password)
                server.sendmail(self.form,self.to,message.as_string())
                print("sent mail successfully")
        except smtplib.SMTPAuthenticationError as e:
            print("SMTP Authentication Error:", e)