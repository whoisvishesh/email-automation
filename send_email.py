import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from datetime import date

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

    # Format the email body using the specified template
    # body = template['body'].format(name=name, due_date=due_date, invoice_no=invoice_no, amount=amount)

    # msg.set_content(body)
    msg.set_content(
        f'''\
        Hi <strong>{name}</strong>,
        I hope you are doing well.

        This is a final reminder that payment for the invoice <strong>{invoice_no}</strong> is due on <strong>{due_date}</strong>.
        The outstanding amount is Rs. <strong>{amount}/-</strong>.

        If payment is not received by the due date, we will need to take further action.

        Please let me know if there are any questions or concerns regarding this invoice.

        Best regards,
        Whoisvishesh
        '''

    # template_2 = {
    #   'subject': 'Final Payment Reminder: Last day',
    #  'body': '''\
    # Hi <b>{name}</b>,

    # I hope you are doing well.

    # This is a final reminder that payment for the invoice <b>{invoice_no}</b> is due <b>{due_date}</b>.
    # The outstanding amount is Rs. <b>{amount}/-</b>.

    # If payment is not received today, we will need to take further action.

    # Please let me know if there are any questions or concerns regarding this invoice.

    # Best regards,
    # Whoisvishesh
    #       '''
    # }'''

    )

    msg.add_alternative(
        f'''\
        <html>
            <body>
                <p>Hi <strong>{name}</strong>,</p>
                <p>I hope you are doing well.</p>

                <p>This is a final reminder that payment for the invoice <strong>{invoice_no}</strong> is due on <strong>{due_date}</strong>.</p>
                <p>The outstanding amount is Rs. <strong>{amount}/-</strong>.</p>
        
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


if __name__ == "__main__":
    send_email(
        subject="Payment Reminder: Due Date is near.....",
        name="Vishesh Chintan",
        receiver_email="whoisvishesh@gmail.com",
        due_date="25th APRIL 2023",
        invoice_no="INV-21-12-009",
        amount="5",
    )
