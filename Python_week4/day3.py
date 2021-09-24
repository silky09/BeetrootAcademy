"""
1. Convert existing friends records from separate variables to
lists:
friends = [
["Anita Reynolds", "anita.reynolds@example.com", 18, True],
["Carl Steward", "carl.steward@example.com", 21, False],
# Other friends ...
]

2. Using the 'for' loop, print out the list of all friends in the
format "<Friend Name>, <age> years old. Email: <friend
email>" (one line per friend).
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

friends = [
    [friend_1_name, friend_1_age, friend_1_email, friend_1_the_best],
    [friend_2_name, friend_2_age, friend_2_email, friend_2_the_best],
    [friend_3_name, friend_3_age, friend_3_email, friend_3_the_best]
]

print(*friends, sep="\n")

print()

#printing friend list using for loop
for i in friends:
    del i[3]
    #i.insert(1, "years old")
    print("Name: {}\nAge: {}\nEmail: {}\n".format(*i), sep='\n')

print("Best friends name:\n")
for friend in friends:
    print(friend[0])














