import random
import math

lower = int(input('Enter first number: '))
higher = int(input('Enter second number: '))

x = random.randint(lower , higher)
print("\n\tYou've only ",
       round(math.log(higher - lower + 1, 2)),
      " chances to guess the integer!\n")

count = 0
while count < math.log(higher - lower + 1, 2):
    count += 1

    guess = int(input('Gues a number: '))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too large!") 

    if count >= math.log(higher - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")




 