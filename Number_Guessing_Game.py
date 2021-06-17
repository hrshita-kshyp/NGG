import random
number = random.randint(1, 10)
player_name = input("Hello, What's your name?")
number_of_guesses=0

print('okay! '+ player_name+'\t' 'Guess a number between 1 and 10:')
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')










