# Quiz: Adding Values to Nested Dictionaries
# Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:

# >>> print(elements['hydrogen']['is_noble_gas'])
# False
# >>> print(elements['helium']['is_noble_gas'])
# True

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

# hydrogen=elements['hydrogen']
# hydrogen.update({'is_noble_gas': False})

# helium=elements['helium']
# helium.update({'is_noble_gas': True})

# print(elements)

# print(elements['hydrogen']['is_noble_gas'])
# print(elements['helium']['is_noble_gas'])

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

elements['oxgen'] = {"a":1,'b': 2}
# x=elements['hydrogen']['is_noble_gas']
# print(x)
print(elements)