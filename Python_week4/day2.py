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
"""
Greeting program
"""
import datetime

name = "Silky"
day = datetime.datetime.today()
current_day = day.strftime("%A")
"print(current_day)"
print("Good day " + name + "! " + current_day + " is a perfect day to learn some python.")

Friend_Name = "Silky"
Age = 35
Email = "silky@gmail.com"
print("\n{}\n{} years old \nEmail: {}".format(Friend_Name, Age, Email))
