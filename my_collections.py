import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from datetime import date
import collections

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
with open('.env', 'r') as f:
    sender_email = f.readline().strip()
    password_email = f.readline().strip()


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Engineering College Ajmer", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f'''\
        Hi {name},
        I hope you are doing well.

        This is a final reminder that payment for the invoice {invoice_no} is due on {due_date}.
        The outstanding amount is Rs. {amount}/-.

        If payment is not received by the due date, we will need to take further action.

        Please let me know if there are any questions or concerns regarding this invoice.

        Best regards,
        Whoisvishesh
        '''
    )

    msg.add_alternative(
        f'''\
        <html>
            <body>
                <p>Hi {name},</p>
                <p>I hope you are doing well.</p>

                <p>This is a final reminder that payment for the invoice {invoice_no} is due on {due_date}.</p>
                <p>The outstanding amount is Rs. {amount}/-.</p>

                <p>If payment is not received by the due date, we will need to take further action.</p>

                <p>Please let me know if there are any questions or concerns regarding this invoice.</p>

                <p>Best regards,</p>
                <p>Whoisvishesh</p>
            </body>
        </html>
        ''',
        subtype="html",
    )
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
