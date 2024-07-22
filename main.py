import random

print("Hello there!! \n You want to play? then you are at the right place! \n So moving to our game...")
lowerbound = int(input("Please enter the lower bound:-"))
upperbound = int(input("Please enter the Upper bound:-"))
num = random.randint(lowerbound , upperbound)
print("Now, wishing you a very good luck ")

for i in range(10):

    guess = int(input("Guess the number:- "))

    if guess == num: 
        print("Yeah your answer is right!!! \n Congratuations you won!!!!!")
        break 

    if guess > num:
        print("No its too high from the number")

    if guess < num:
        print("Noo its too low from the number")

else:
    print("You lose \n Better Luck next time")