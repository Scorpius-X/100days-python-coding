import smtplib
import random
import sys
sys.path.append("C:/Users/ALPHONSE/Desktop/GitHub/100days-python-coding")
from secretss import gm_password
import datetime as dt
import pandas
import os
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


my_email = "scorpius791@gmail.com"
recieving_mail = "eric.bolade@gmail.com"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today = (day,month)

output_dir = "C:/Users/ALPHONSE/Desktop/GitHub/100days-python-coding/Day32"
os.makedirs(output_dir, exist_ok= True)

data_dict =  {}
random_letter = [
    "Day32/birthday-wisher-extrahard-start/letter_templates/letter_1.txt",
    "Day32/birthday-wisher-extrahard-start/letter_templates/letter_2.txt",
    "Day32/birthday-wisher-extrahard-start/letter_templates/letter_3.txt"
]
birthday_letter = random.choice(random_letter)


data = pandas.read_csv("Day32/birthday-wisher-extrahard-start/birthdays.csv")
for index,row in data.iterrows():
    key = (row["day"], row["month"])
    value = ",".join(str(v) for v in row.values)
    data_dict[key] = value
    first_word = data_dict[today].split(",")[0]

if today in data_dict:
    with open(birthday_letter, "r") as file:
        content = file.read()
        content = content.replace("[NAME]", first_word)

    date_str = now.strftime("%d-%m-%Y")
    output_file = os.path.join(output_dir, f"{first_word}_letter_{date_str}.txt")

    with open(output_file, "w") as file:
        file.write(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user = my_email, password= gm_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= recieving_mail,
            msg= f"Subject: Happy Birthday!\n\n{content}"
        )

    

