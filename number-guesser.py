import random

# r = random.randrange(1,10)#doesnot include the upperbound#
# t = random.randint(1,10)#includes the upperbound
# print(r,t)
random_number = input("Enter a number ")
if random_number.isdigit():
    random_number = int(random_number)
    if random_number <= 0:
        print("Enter a number larger than 0")
        quit()
else:
    print("Enter a number")
    quit()
r = random.randrange(0, random_number)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number next time")
        continue
    if user_guess == r:
        print("You got it right")
        break
    elif user_guess < r:
        print("Your guess is below the actual")
    else:
        print("Your guess is larger than the actual")
    continue
print("You got it right in", guesses, "guesses")
