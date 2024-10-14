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

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print(" car is already started")
        else:
            started = True
            print("car started ready to go")
    elif command == "stop" :
        if not started:
            print(" car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
quit - to quit
         """)
    elif command == "quit":
        break
    else:

        print("sorry, i don't get that")






