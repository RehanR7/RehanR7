import pandas as pd
import datetime as dt
from random import randint
import smtplib

my_email = "rhnather@gmail.com"
password = "qsyz cnds jndl eqgv"
mail_host = "smtp.gmail.com"

def send_mail(host: str, header: str, body: str):
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=item["email"],
            msg=f"Subject: {header}\n\n{body}"
        )

df = pd.read_csv("birthdays.csv")
birthday_records_list = df.to_dict(orient="records")
date = dt.datetime.now()
month, day = date.month, date.day
for item in birthday_records_list:
    if (month, day) == (item["month"], item["day"]):
        pick_letter = randint(1,3)
        with open(f"letter_templates/letter_{pick_letter}.txt") as letter:
            content = letter.read().replace("[NAME]", item["name"])
        send_mail(mail_host, "Happy Birthday!", content)


