# for loop perform the same action for all the items in a list
magicians= ['ahmed','marwa','salwa','bata', 'eman', 'ola']
for magician in magicians:
    print(magician)

magicians= ['ahmed','marwa','salwa','bata', 'eman', 'ola']
for magician in magicians:
    print(f"{magician.title()}, you did a great job")
    print(f" I am looking forward for your next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great show.\n")
