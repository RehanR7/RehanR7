# import smtplib
#
# email = "rhnather@gmail.com"
# to_mail = "rehan_biotech@yahoo.com"
# password = "qsyz cnds jndl eqgv"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=to_mail,
#         msg="Subject: Important Update\n\nHello, this is a test email sent from an automated script.")
# from calendar import weekday
# import datetime as dt
#
# date = dt.datetime.now()
# print(date)
# year = date.year
# print(year)
# month = date.month
# print(month)
# day = date.day
# print(day)
# day_of_week = date.weekday()
# print(day_of_week)
#
# birth_day_date = dt.datetime(year=2001, month=7, day=3)
# print(birth_day_date)

from random import choice
import smtplib
import datetime as dt

def get_quote():
    with open("quotes.txt") as f:
        quotes = [line.strip() for line in f]
        return choice(quotes)

def get_current_date():
    date = dt.datetime.now()
    week_day = date.weekday()
    return week_day

email = "rhnather@gmail.com"
to_mail = "rehan_biotech@yahoo.com"
password = "qsyz cnds jndl eqgv"

if get_current_date() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_mail,
            msg=f"Subject: Monday Motivation\n\n{get_quote()}"
        )







