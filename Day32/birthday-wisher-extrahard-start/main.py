##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime as dt
import random
import pandas as pd
import os
from secretss import gmail_password

my_email = "scorpius791@gmail.com"
recieving_mail = "eric.bolade@gmail.com"

now = dt.datetime.now()
year = now.year
today_month = now.month
dayoftheweek = now.weekday()
today_day = now.day
today = (today_day,today_month)
print(today)

data = pd.read_csv("Day32\\birthday-wisher-extrahard-start\\birthdays.csv")

data_dict = {}

#creates an output directory so that i can save the newly modified birthday letter
output_dir = "Day32\\birthday-wisher-extrahard-start\\readytosend"
os.makedirs(output_dir, exist_ok= True)

#looped into the df and append the key and value in a tuple key : value format

for index,row in data.iterrows():
    key = (row["day"],row["month"])
    value = ",".join(str(v) for v in row.values)
    data_dict[key] = value

#store the relative paths of the letter templates in a list and use the random module to pick a letter
random_letter = [
    "Day32\\birthday-wisher-extrahard-start\\letter_templates\\letter_1.txt",
                 "Day32\\birthday-wisher-extrahard-start\\letter_templates\\letter_2.txt",
                 "Day32\\birthday-wisher-extrahard-start\\letter_templates\\letter_3.txt"]

#checks if the day and time today matches the celebrants date of birth
if today in data_dict:
    birthdayletter = random.choice(random_letter)

    with open(birthdayletter, "r") as file:
        letter = file.read()
        first_word = data_dict[today].split(",")[0]
        print(first_word)
        letter = letter.replace("[NAME]", first_word.upper())

    #uses the datetime module to save the newly modified letter with the date and month to track it
    date_str = dt.datetime.now().strftime("%d-%m-%Y")
    output_file = os.path.join(output_dir, f"{first_word}_letter_{date_str}.txt")

    with open(output_file, "w") as file:
        file.write(letter)
        print(letter)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user= my_email, password= gmail_password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= recieving_mail, 
            msg= f"Subject:Happy Birthday!\n\n{letter}")







