from datetime import date
import pandas as pd
from send_email import send_email, template_1

sheet_id = "1rOQW0p4p1v2OC-UL-T2VpXCTeNLwWCM8I5n0mx_iEJ8"
sheet_name = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"


def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def send_emails_using_data(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if(present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                template_1,
                name=row["name"],
                receiver_email=row["email"],
                due_date=row["due_date"].strftime("%d, %b %Y"),
                invoice_no=row["invoice_no"],
                amount=row["amount"]
            )

            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


df = load_df(URL)
result = send_emails_using_data(df)
print(result)
