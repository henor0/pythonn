fruts = ["apple", "banana", "cherry"]

print(fruts)

#Create a tuple
words = ("spam", "eggs", "sausages")
print(words[1])

#Creating a tuple with information about a person

person = ('Blerta', 24, "Engineer")

name, age, proffesion = person

print (name, "'s", "profession is", proffesion, "and she is", age, "years old.")



person = ('Henor', 17, "Radiolog")

name, age, proffesion = person

print (name, "'h", "proffesion is", proffesion , "and she is", age, "years old")

#Creating dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",

    #more keys more values pairs
}


contact_info = {
    "Blerta": "444-333405",
    "Drini" : "3339-3333"
}

#Creating a variable called Kreative's phonr and use [] we can spcify wich key we want to access

kreative_phone = contact_info ["Blerta"]

print(kreative_phone)
print(contact_info)

contact_info ["Drini"] = "0294-48575"

print(contact_info)

#We want to add another friend to contact_info

contact_info ["Eros"] = "9384-117348"

print(contact_info)

#Delete a contact info

del contact_info ["Blerta"]
print(contact_info)

keys = contact_info.keys()

print(keys)

#Print only the keys of the dictionery

keys = contact_info.keys()

print(keys)

#print Values
values = contact_info.values()
print(values)

#print items
item = contact_info.items()
print(item)

