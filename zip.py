names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# want to loop over both lists and print in sync
# one way using enumerate
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# another way is by using zip
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

# can even add more lists
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heroes, universes):
    print(value)