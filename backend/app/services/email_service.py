import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings


class EmailService:

    @staticmethod
    async def send_email(to, subject, body):
        """
        Sends an email using the provided parameters.

        Parameters:
        - to (str): The recipient's email address.
        - subject (str): The subject of the email.
        - body (str): The body content of the email.

        Returns:
        - None

        Note:
        - This method uses settings.MAILTRAP_USERNAME and settings.MAILTRAP_PASSWORD to authenticate with the email server.
        - The email is sent from 'password-reset@{settings.BASE_URL}'.
        - The email server used is 'smtp.mailtrap.io' on port 587.
        - If an error occurs during the email sending process, an exception is raised and an error message is printed.

        """
        mail_content = body

        sender_address = settings.MAILTRAP_USERNAME
        sender_pass = settings.MAILTRAP_PASSWORD
        receiver_address = to

        message = MIMEMultipart()
        message['From'] = f"password-reset@{settings.BASE_URL}"
        message['To'] = receiver_address
        message['Subject'] = subject

        message.attach(MIMEText(mail_content, 'plain'))
        text = message.as_string()

        try:
            with smtplib.SMTP('smtp.mailtrap.io', 587) as server:
                server.starttls()
                server.login(sender_address, sender_pass)
                server.sendmail(sender_address, receiver_address, text)
                print('Email sent successfully')
        except Exception as e:
            print('Error, email not sent: ', e)
