

#Lets create a list
al=['a','b','c','d']

#To print all elements of a list we use (:) or (*)
print('All the elements in list')
print(al)
print(al[:])

#To return elements without , and brackets.
print('All the elements without comma')
print(*al)

#To print single elements we use index. First element is at 0 index, second element at 1 and so on.
print('Displaying single element at index place')
print(al[0])
print(al[1])

#To print range of element or multiple elements. Following code will return first three elements of list.
print('Following are element for the range of indices from 0 to 3')
print(al[0:3])

#To print last item use  minus (-) sign to return last one. Following code will return last element.
print('This will return elements in last place')
print(al[-1])

# Printing list seperated by comma.
print('Displaying list elements by using comma in between them')
print(*al, sep = ',')


# Printing list's elements on new line
print('Displaying each element on new line')
print(*al, sep = '\n')

# Following line of code returns truncated elements list from left to right.
print('Displaying truncated element, will show only elements of indices 2 and forth indices')
print(al[2:])

# Following line of code returns truncated elements list from right to left.
print('Displaying truncated element, will show only elements of indices 3 and back indices')
print(al[:3])
                                     # changing or updating list elements
                                    
# Updating single element in a list.
print('This will update value of element at index 2')
al[2] = 23
print(al)

# Again updating element at index 2 to its orginal one.
print('Again we can update integer value to string')
al[2] = 'b'
print(al)

# updating all elements with same change by using for loop.
#appending b with all elemenets
print('In following we are updating all the elements with same value added')
for i in range(len(al)):
     al[i] = al[i] + 'b'

print(al)
                                # Removing elements from list.

# Removing single elements from list.
print('Removing element at index 1')
del al[1]
print(al)

# Another method to remove an element is pop method. What pop do, it delete and returns deleted element to on screen.
print('Removing specific element and returning deleted element')
print(al.pop(2))
print('Here is now orignal list after using pop method')
print(al)

# logical error may occurs, if we want to remove multiple element at once by using del(al[0]); del(al[1]. This will not delete desire element because of del well excute twice
# once del excute and delete element at index 0. After deletion place of each element will shift one step towards zero. Now when del systax extuce agian it delete different
# element at index 1. To avoid this error we used following code.
print('deleting range of an element or multiple element')
del(al[0:1])
print(al)

                                # adding new elements to the list

print('Here we are adding elements to a list')
al2 = al + ['beautifull', 5]
print(al2)
                                # Assing and copy
print('The following code assign list to another list')
al3 = al2
print('list al3 will have same element in al2')
print(al3)

# but problem comes when we changes something in al2, al3 also affects, to avoid this problem and keeping the orignal al2 list same we use following code
al3 = list(al2)
al3[0] = 'amazing'
print('copy list al3 has changed ')
print(al3)
print('But the orginal list al2 is same as earlier')
print(al2)
