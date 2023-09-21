import random  # get the function from the lib
import math  # get the function from the lib
# taking input from the user
lower = int(input("ENTER YOUR LOWER RANGE:- "))

# taking input from the user
upper = int(input('ENTER YOUR UPPER RANGE:- '))
# generating random numbers between the lower and the upper bound
# random.randint() is a function that returns a random integer value
x = random.randint(lower, upper)
print(" You have only",
      # round is a function that rounds up number from (1-10)
      round(math.log(upper - lower + 1, 2)),

      "chances to guess your to a number ", lower, "-", upper)
# adding the number guess

count = 0
# this helps to define the number of
while count < math.log(upper - lower + 1, 2):
    # THIS code math.log()
    # brings out the log of the upper number
    # and makes the base of the lower number
    count += 1

# To receive user input data and it most be an integer
    guess = int(input())
    if int(input()) == '':
        print("PLEASE YOU NEED TO INPUT A NUMBER BETWEEN", upper, "&", lower)
        break
# The section to ensure that the guess number is
# not less than or greater than then range number
    if guess <= lower:  # if the input is less than the range
        print('NUMBER IS LOWER THAN LOWER RANGE')
        break  # end code if the above statement is correct
    elif guess >= upper:  # if the input is higher than the range
        print('NUMBER IS HIGHER THAN THE UPPER RANGE')
        break
# To check the input is equal to
#  number the computer chooses
    if guess == x:
        # if the number the user input is equal to the ranged number
        print("THE NUMBER", count, "IS CORRECT DO HAVE A NICE DAY")
        #  when the statement is said to true
        break  # this is to end the code if the statement is true

    elif guess < x:  # if the input is less than the range
        print("TRY AGAIN YOUR GUESS", guess, "IS TOO LESS THAN THE NUMBER")
    elif guess > x:  # if the input is greater than the ranged
        print("TRY AGAIN YOUR GUESS ' ", guess,
              " 'IS TOO HIGHER THAN THE NUMBER")


# this is to check the number of attempt you can go through before the code end
if count >= math.log(upper - lower + 1, 2):
    print("You have successfully used your limit")
else:
    count += 1
    # if a number of attempt is selected this helps to increase the attempt time before is comes to the end
