import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
from utils import Utils

class Mailer:

    def send_mail(self, reciever):
        utils = Utils()
        email_user = utils.report_mailer["mail-id"]
        email_password = utils.report_mailer["mail-password"]
        email_send = reciever
        subject = str(date.today())+'ZOOM RECORDINGS UPLOAD REPORT'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Successfully Uploaded Zoom recordings to Vimeo.The generated reportfile is attached below.'
        msg.attach(MIMEText(body, 'plain'))

        filename = 'outputfile.csv'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        print('\n'+' Mail Has Been Sent To {filename} '.format(filename=reciever).center(100,':'))

        server.quit()
