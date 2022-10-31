                                            # Methods
# Methods are functions thats  belongs to Objects. veriable like intergers, strings and float are Objects
# index() is a method. we use index() to find any element's index in a list.
# let suppose we have list fam
from re import A


fam = ['dad', 35, 'mom', 30, 'bro', 18, 'sis', 12]
print('calling index method to find index of mom')
print(fam.index('mom'))

# To explore other methods lets declare some veriable. Using upper() method, converting string from lower to upper
nam ='Umar Ali'
print('Changing nam from lower to uppercase')
print(nam.upper())
# Calling method to count specific letter or entire word's lettters.
print('Find nuumber of As in string nam')
print(nam.count('A'))
 # Calling count function in list fam.
print('Find the count dad in list fam')
print(fam.count('dad'))
print('finding letter S in list element sis')
print(fam.count('sis'))

# Calling methods of append and reverse.
fam.append('bro')
fam.append(20)
print('fam list after appending new data')
print(fam)
print('Reverse order of an elements')
fam.reverse()
print(fam)
# calling method to remove an element from list.
fam.remove('sis')
print('Here is the list after removed element')
print(fam)
