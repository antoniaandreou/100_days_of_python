import smtplib
import datetime as dt
import random

def email_enginee(quote:str):
    from_email = "??????@gmail.com"
    password = "??????"
    recipient_email = "?????@yahoo.com"

    # Creating an object from the SMTP class
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        # TLS stands for Transport Layer Security
        # starttls ==> A way of securing our connection to the email server by encrypting our email
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Motivational Quote \n\n {quote}")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    try:
        with open("motivational_quotes/quotes.txt", "r") as quotes:
            all_quotes = quotes.readlines()
            todays_quote = random.choice(all_quotes)
            email_enginee(todays_quote)
            print(todays_quote)
    except FileNotFoundError:
        print("Quotes file not found")


