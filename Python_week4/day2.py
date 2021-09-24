"""
1. Use variables to create several records for friends in the
following format:
friend_1_name = "Anita Reynolds"
friend_1_email = "anita.reynolds@example.com"
friend_1_age = 18
friend_1_the_best = True # or False in case if this
person is not your best friend

friend_2_name = "..."
friend_2_email = "..."
# ...

2. Print out any friend in the format "<Friend Name>, <age>
years old. Email: <friend email>"
"""

friend_1_name = "Anita Reynolds"
friend_1_email = "anita.reynolds@example.com"
friend_1_age = 18
friend_1_the_best = True

friend_2_name = "Zoe pal"
friend_2_email = "zoe.pal@example.com"
friend_2_age = 28
friend_2_the_best = False

friend_3_name = "Ane Reyon"
friend_3_email = "ane.reyon@example.com"
friend_3_age = 38
friend_3_the_best = True

print("\n{}\n{} years old \nEmail: {}".format(friend_3_name, friend_3_age, friend_3_email))

print()

"""
Greeting program
"""

import datetime

name = "Silky"
language = "python."
current_day = datetime.datetime.today()
day = current_day.strftime("%A")
"print(current_day)"
print("Good day " + name + "! " + day + " is a perfect day to learn some " + language)

"""Friend_Name = "Silky"
Age = 35
Email = "silky@gmail.com"
print("\n{}\n{} years old \nEmail: {}".format(Friend_Name, Age, Email))"""
