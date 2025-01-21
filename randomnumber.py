import random
playing=True
number=str(random.randint(0,10))
print("Now,I will generate the number from 0 to 5 hen,you have to guess the number")
print("If,you win you will get a point")
while playing:
    guess=input("Enter your guess")
    if number==guess:
        print("Your guess is correct")
        break
    else:
        print("Your guess is incorrect try it agait")
        print("Have a good luck at next try")