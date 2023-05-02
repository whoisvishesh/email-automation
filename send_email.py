import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
with open('.env', 'r') as f:
    sender_email = f.readline().strip()
    password_email = f.readline().strip()

# Define email templates
template_1 = {
    'subject': 'Payment Reminder',
    'body': '''\
        Hi {name},
        I hope this email finds you well.

        This is just a friendly reminder that payment for the invoice {invoice_no} is due on {due_date}. 
        The outstanding amount is Rs. {amount}/-.

        Please let me know if there are any questions or concerns regarding this invoice.

        Best regards,
        xyz firm
    '''
}

template_2 = {
    'subject': 'Final Payment Reminder',
    'body': '''\
        Hi {name},
        I hope you are doing well.

        This is a final reminder that payment for the invoice {invoice_no} is due today. 
        The outstanding amount is Rs. {amount}/-. 
        If payment is not received today, we will need to take further action.

        Please let me know if there are any questions or concerns regarding this invoice.

        Best regards,
        YOUR NAME
    '''
}


def send_email(template, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = template['subject']
    msg["From"] = formataddr(("Engineering College Ajmer", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    # Format the email body using the specified template
    body = template['body'].format(name=name, due_date=due_date, invoice_no=invoice_no, amount=amount)

    msg.set_content(body)

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    # Send the first email reminder
    send_email(
        template_1,
        name="Vishesh Chintan",
        receiver_email="whoisvishesh@gmail.com",
        due_date="25th APRIL 2023",
        invoice_no="INV-21-12-009",
        amount="5",
    )

    # Send the final email reminder
    send_email(
        template_2,
        name="Vishesh Chintan",
        receiver_email="whoisvishesh@gmail.com",
        due_date="30th APRIL 2023",
        invoice_no="INV-21-12-009",
        amount="5",
    )
