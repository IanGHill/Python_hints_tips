class Person():
    pass

person = Person()

# person.first = "Ian"
# person.last = "Hill"
#
# print(person.first)
# print(person.last)

first_key = 'first'
first_val = 'Ian'

# setattr(person, 'first', 'Ian')  this works but can also use variables as below:
setattr(person, first_key, first_val)
print(person.first)

first = getattr(person, first_key)
print(first)


person_info = {'first': 'Ian', 'last': 'Hill'}

for key, value in person_info.items():
    setattr(person, key, value)
print(f'{person.first} {person.last}')

for key in person_info.keys():
    print(getattr(person, key))
