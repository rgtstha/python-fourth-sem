# Create a phonebook of your friends
# using dictionary in python.

# print all friend's name
# get the mobile number of specific friend
# using  get() method


phonebook = {
    'ram': 9843124385,
    'sita': 980867385,
    'bob': 9860346848,
}

for key in phonebook:
    print(key)

print(f"Phone number of ram is {phonebook.get('ram')}")