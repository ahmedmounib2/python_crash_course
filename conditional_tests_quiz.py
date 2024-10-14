# while loops
i= 1
while i <= 5:
    print('*'*i)
    i = i +1
print('done')

secret_guess = 9
guess_count = 0
guess_limit = 3
while guess_count< guess_limit:
    guess = int(input('guess: '))
    guess += 1
    if guess == secret_guess:
        print('you won')
        break



# while loops
i= 1
while i <= 5:
    print('*'*i)
    i = i +1
print('done')

secret_guess = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_guess:
        print('you won')
        break
else:
    print('you lost')



