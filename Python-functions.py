                                                                #Functions
# A function is block of code which only runs when it is called. You can pass data, which is called parameters or arguments, into a function.
# print(), type(), len(), max(), round() all are built-in function in python.

# Let create a list
var1 = [4,3,2,1]
var4 = [5,6,7,8]
# and a bolean veriable
var2 = True

# Now we are going to call type() function first. keep in mind function only works when it is called.
print('Type of var1 is:')
print(type(var1))

# length is the another important function which return length of a veriable. Extermly usefull can be used to find character in a string.
print('This will return length of var1')
print(len(var1))
# trying to find length of bolean will result in an error because bolean variable has no length, i.e. print(len(var2)) will result in error.

# another important function is converting one type of variable into another type.
print('In this example we are converting bolean into intger')
var3 = int(var2)
print('In following you can see the converted type.')
print(type(var3))

# Another useful function is help(), which can provide help about any function. ? can also be used to find help about function.
print('help about power function')
help(pow)

# max() is another usefull function to find maximum value in list.
print('Maximuum value in var1')
print(max(var1))

# with power function we can find exponent of any interger or float.
print('Find power of interger and float')
print(pow( 5, 2, mod=None))
print(pow( 3.3, 2, mod=None))


# Another important function is sorted function which help to organise data in ascending or desending orders.
# first we concatenate to list var1 and var3 togather to make list bigger for data sorting
# it is necessary for concatenation that all list should be in same data type, if both type are of different type convert...
# them using variable conversion function
print('Cocatenating + operator var1 and var3 togather')
ful1 = var1 + var4
print(ful1)
# Another way to concatenate list is using for loop.
for i in var1 : var4.append(i)
print ("Concatenated list using naive method : " 
                              + str(var4))
# sorting in descending order
print('Calling sorted function to sort lists')
full_sorted = sorted(ful1, reverse= True)
print('Here is full sorted list in desending order')
print(full_sorted)
# sorting in ascending order
print('Calling sorted function to sort lists')
full_sorted = sorted(ful1, reverse= False)
print('Here is full sorted list in ascending order')
print(full_sorted)

# There almost built in function for every task in python, but you can make and define your own, as shown in following
# First we define function. In our function, it calculate and return area of a rectangle or square.

def areaCal(len, wid):
     print( len * wid )

areaCal(6,4)

# keyword return function end the function call and returns the result to the caller. 
# The statement after return statement are not excuted.
# here is example function with return statement. which returns result as for as statement is true and return 0 right after...
# after when statement become false.
def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)




