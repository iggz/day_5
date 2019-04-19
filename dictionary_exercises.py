##################
### Exercise 1 ###
##################

# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict['Elizabeth'])

# phonebook_dict['Kareem'] = '938-489-1234'

# print(phonebook_dict)

# del phonebook_dict['Alice']

# print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'

# print(phonebook_dict)

# print(phonebook_dict.values())


##################
### Exercise 2 ###
##################

# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#     {
#         'name': 'Jasmine',
#         'email': 'jasmine@yahoo.com',
#         'interests': ['photography', 'tennis']
#         },
#     {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'tv']
#         }
#     ]
# }

# print(ramit['email'])
# print(ramit['interests'][0:1])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])


######################
### Letter Summary ###
######################

# word = input("Please enter word ")
# dict = {}

# def letters():
#     for i in word:
#         if i in dict:
#             dict[i] += 1
#         elif i not in dict:
#             dict[i] = 1
#     return(dict)

# print(letters())



# ####################
# ### Word Summary ###
# ####################

# # sentence = input("Please enter a sentence: ")
# string = "To be or not to be"

# def summary(str):
#     # need to break up sentence into individual words
#     dict = {}
#     lower_string = str.lower()
#     split_string = lower_string.split()
#     for i in split_string:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict

# print(summary(string))

#######################
### Bonus Challenge ###
#######################

# sentence = input("Please enter a sentence: ")
string = "To be or not to be to or to be"

def max_val(str):
    dict = {}
    string_lower = str.lower()
    string_split = string_lower.split()

    for i in string_split:
        if i in dict:
            dict[i] += 1
        if i not in dict:
            dict[i] = 1

    dict_values = []
    for value in dict.values():
        if value > dict_values:
            dict_values = value
    return 
        



print(max_val(string))



