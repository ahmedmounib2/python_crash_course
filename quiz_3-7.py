friends=['ola','ahmed','farida']
popped_friend= ['not attending']
friend = friends[0]
print(f"Hi {friend}, You are invited to my party, its friday at 8 pm at my place")
x= input('are you coming to my party, reply: with yes or no?  ')
if x == "yes":
    print(f"{friend} , 'attending next friday'")

else:
    friends.pop(0)
    popped_friend= ['']
    popped_friend.append('ola')
    print(f"{popped_friend}, is not attending.")
    print(friends)

friends=['ola','ahmed','farida']
friend = friends[1]
print(f"Hi {friend}, You are invited to my party, its friday at 8 pm at my place")
x= input('are you coming to my party, reply: with yes or no?  ')
if x == "yes":
    print(f"{friend} , 'attending next friday'")

else:
    friends.pop(1)
    popped_friend.append('ahmed')
    print(f"{popped_friend}, is not attending.")
    print(friends)

friends=['ola','ahmed','farida']
friend = friends[2]
print(f"Hi {friend}, You are invited to my party, its friday at 8 pm at my place")
x= input('are you coming to my party, reply: with yes or no?  ')
if x == "yes":
    print(f"{friend} , 'attending next friday'")

else:
    friends.pop(2)
    popped_friend.append(2)
    print(f"{popped_friend}, is not attending.")
    print(friends)
print('found a bigger table, i will invite sandra rika and maria')
friends.insert(0,'rika')
friends.append('sandra')
friends.insert(2,'maria')
print(friends)
print(popped_friend)


