import datetime as dt
import pandas as pd
import random
import smtplib


def email_enginee(subject: str, msg_body: str, recipient_email="????????@yahoo.com"):
    from_email = "??????@gmail.com"
    password = "?????"

    # Creating an object from the SMTP class
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        # TLS stands for Transport Layer Security
        # starttls ==> A way of securing our connection to the email server by encrypting our email
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:{subject} \n\n {msg_body}")


# ------------------ MAIN ------------------- #
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthdays = pd.read_csv("birthday_wishes/birthdays.csv")
bday_dict = {(data_row.month, data_row.day): data_row.to_list() for (index, data_row) in birthdays.iterrows()}

if today in bday_dict:
    name = bday_dict[today][0]
    letter_choice = random.randint(1, 3)
    with open(f"birthday_wishes/letter_templates/letter_{letter_choice}.txt") as letter:
        letter_content = letter.read()
        amended_letter = letter_content.replace("[NAME]", name)

    email_enginee("Happy Birthday!", amended_letter, "?????@gmail.com")
