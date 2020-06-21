names = ['Ian', 'Max', 'Dave', 'John']

# non-pythonic way to do it
index = 0
for name in names:
    print(index, name)
    index += 1

# pythonic way of doing it
for index, name in enumerate(names, start=1):
    print(index, name)