print("Welcome to MyFriends 1.0!")
print()
"""
Homework. Advanced level

write a program, which has two print statements to print
the following text (capital letters “O” and “H” made out of “#” symbols):

#####
#   #
#   #
#   #
#####

#   #
#   #
#####
#   #
#   #
"""



print()



for row in range(7):
    for col in range(5):
        if row in {0, 1, 2, 4, 5, 6} and col in {0, 4}:
            print('#', end=' ')
        elif row == 3:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()

print()


for row in range(7):
    for col in range(5):
        if row in {0, 6} and col in {1, 2, 3}:
            print('#', end=' ')
        elif row in {1, 2, 3, 4, 5} and col in {0, 4}:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()
