import random
guesses = 0
n = random.randint(0, 100)
name = input("Hello what is your name: ")



print("Enter an integer from 0 to 100: ", end='')
guess = int(input())

while n != guess:
    
    if (n < guess):
        print ("Number is LOWER")
        guesses = guesses + 1
        print("Enter an integer from 0 to 100: ", end='')
        guess = int(input())
    elif (n > guess):
        print ("Number is HIGHER")
        guesses = guesses + 1
        print ("Enter an integer from 0 to 100: ", end='')
        guess = int(input())
    # end if

# end while loop
guesses = guesses + 1
print ("Congratulations" ,name,  "it took you" ,guesses, "guesses to get the number" ,n)