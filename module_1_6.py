my_dict = {'Vlad': 1997, 'Artem':2000}
print(my_dict)
print(my_dict['Vlad'])
my_dict.update({'Denis': 1996,
                'Ilnur': 1999})
del my_dict['Artem']
print(my_dict.get('Artem'))
print(my_dict)

my_set = {1, 2, 3, 1, 2, 'Vlad', 26.11}
print(my_set)
my_set.add(5)
my_set.add('Isanov')
my_set.remove('Vlad')
print(my_set)