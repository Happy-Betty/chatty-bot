print("Hello, my name is Chatty")
print("I was created in 2021")
print("Please, remind me your name")
Name = input("enter your name right here: ")
print("what an amazing name " + Name + '.' + " It's a pleasure meeting you")
print("Let me guess your age ")
print("But first you will help me with something small")
print("Enter remainders of your age after dividing by 3, by 5 and by 7 respectively: ")
#  capturing the remainders of the user's age
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
# formula for finding the user's age
user_age = ((remainder3 * 70) + (remainder5 * 21) + (remainder7 * 15)) % 105

print("Your age is " + str(user_age) + " ; that's a good time to start programming!")