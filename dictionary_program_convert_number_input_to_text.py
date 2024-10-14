# dictionary in python
#name: John Smith
#email:john@gmail.com
#phone:1234

# dictionary defined with {}, no duplicates ALLOWED, case sensitive
customer = {
    "name": "John Smith",
    "age":30,
    "is_verified": True
}
print(customer["name"])

#instead of getting key error for searching for something that is not in the dictionary
# get method wil lreturn none as below
print(customer.get("birthdate"))

print(customer.get("birthdate","jan 1 1980"))

#updating a key value
customer["name"] = "Jack Smith"
print(customer["name"])

phone = input("phone: ")

digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") +" "
print(output)
