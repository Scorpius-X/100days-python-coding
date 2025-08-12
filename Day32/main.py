import smtplib
import datetime as dt
import sys
sys.path.append("C:/Users/ALPHONSE/Desktop/GitHub/100days-python-coding")
from secretss import gm_password
import random


my_email = "scorpius791@gmail.com"
recieving_mail = "eric.bolade@gmail.com"



now = dt.datetime.now()
year = now.year
month = now.month
dayoftheweek = now.weekday()
if dayoftheweek == 0:
    with open("Day32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user= my_email, password= gm_password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= recieving_mail, 
            msg= f"Subject:Motivational Quote\n\n{quote}")
