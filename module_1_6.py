my_dict={'бабушка':1908,'дедушка':1906,'мама':1939}
print('my_dict до изменений:',my_dict)
print('существующее значение:',my_dict['мама'])
print('не существующее значение:',my_dict.get('внук','не родился пока...'))
my_dict.update({'сестра':1992,'тётя':1954})
print('удаленное значение:',my_dict.pop('дедушка'))
print('my_dict после изменений:',my_dict)

my_set={1,3,4,2,5,6,1,5,'слово',7,2,'слово',(3,False,'АБВГД')}
print('my_set до изменений:',my_set)
my_set.add(3.1415926535)
my_set.add('добавлено')
my_set.discard(5)
print('my_set после изменений:',my_set)