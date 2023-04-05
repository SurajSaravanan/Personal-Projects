#!/usr/bin/env python
# coding: utf-8

# ## Project 3 - 100 points
# 
# Please complete this Python notebook and upload it to the Project 3 locker.
# This project is meant to familiarize you with basic data structures and data manipulation in Python.
# 

# In[1]:


# 1 Extracting substrings. Write a SINGLE python statement to slice the below string and extract 'srwer' from it 
# When executed, this block should produce the output 'srwer'                                                   - 3 points

strobj = 'strawberry'

strobj[0:len(strobj):2]


# In[6]:


# 2 Write a for loop to iterate through the string and to print all vowels within it  
# When executed, this block should output all vowels in the string                                              - 3 points

strobj = 'strawberry'

for char in strobj:
    if char in 'aeiouAEIOU':
        print(char)


# In[8]:


# 3 Write python statement/statements to duplicate both strings and to join them to produce String1String1String2String2
# When executed, this block should produce the output 'String1String1String2String2'                            - 3 points

str1 = 'String1'
str2 = 'String2'


print(str1+""+str1+""+str2+""+str2)


# In[16]:


# 4 Write python statements to covert the below string to all uppercase and all lowercase.
# When executed, this block should produce the output CONVERTCASE  convertcase                                  - 3 points

strobj = 'ConvertCase'

upper = strobj.upper()

print("{}".format(upper))

lower = strobj.lower()

print("{}".format(lower))


# In[19]:


# 5 Write a python statement to change item at index 2 to 'bmw'                                                   
# When executed, this block should produce the output ['bus', 'bike', 'bmw', 'toyota']                          - 3 points

lst = ['bus', 'bike', 'honda', 'toyota']

lst[2] = 'bmw'
print(lst)


# In[20]:


# 6 Write a python statement to create a new list lst3 that is a result of joining two lists
# When executed, this block should produce the output ['bus', 'bike', 'bmw', 'toyota']                          - 3 points

lst1 = ['bus', 'bike']
lst2 = ['bmw', 'toyota']

concatlist = lst1 + lst2
concatlist


# In[24]:


# 7 Iterate through the list to check if 'apple' is present in the list
# When executed, this block should produce the output True                                                      - 3 points 

lst = ['banana', 'peach', 'pear', 'apple']

for item in lst:
    if item == 'apple':
        print('True')
        


# In[29]:


# 8 Iterate through the list to check if 'mango' is present in the list. If not append it to the list.            - 3 points
# When executed, this block should produce the output ['banana', 'peach', 'pear', 'apple', 'mango']


lst = ['banana', 'peach', 'pear', 'apple']

for item in lst:
    if item == 'mango':
        print('True')
        
lst.append('mango')
lst


# In[30]:


# 9 Remove the item 'pear' from the below list.
# When executed, this block should produce the output ['banana', 'peach', apple', 'mango']                      - 3 points

lst = ['banana', 'peach', 'pear', 'apple', 'mango']

lst.remove('pear')
lst


# In[36]:


# 10 Iterate through the list to remove numbers that are divisible by 4 from the list
# When executed, this block should produce the output [35, 31, 13]                                              - 3 points

lst = [24, 35, 40, 31, 13]

for item in lst:
    if item % 4 == 0:
        lst.remove(item)
lst


# In[38]:


# 11 Write a python statement to convert the below tuple to a list
# When executed, this block should produce the output ['banana', 'peach', 'apple', 'mango']                      - 3 points

tup = ('banana', 'peach', 'apple', 'mango')

mylist = list(tup)

mylist


# In[39]:


# 12 Write a python statement to conver the below list to a tuple
# When executed, this block should produce the output ('banana', 'peach', 'pear', 'apple')                      - 3 points

lst = ['banana', 'peach', 'pear', 'apple']

mytup = tuple(lst)

mytup


# In[40]:


# 13 Write python statements to replace peach with grape in the below tuple. 
# When executed, this block should produce the output ('banana', 'grape', 'pear', 'apple')                      - 3 points
# Hint: Tuples are immutable so think of converting the tuple to a different data structure,
# make the changes and convert it back to a tuple

tup = ('banana', 'peach', 'pear', 'apple')

mylist = list(tup)
mylist[1] = 'grape'

mytup = tuple(mylist)
mylist


# In[41]:


# 14 Find number of items in the tuple
# When executed, this block should produce the output 3                                                          - 3 points

tup = (5, 2, 8)
len(tup)


# In[4]:


# 15 Iterate through the tuple and every time you encounter an odd number, append it to a new list and print the list
# When executed, this block should produce the output [3, 5, 9]                                                  - 4 points

tup = (2, 3, 5, 8, 10, 9, 6)
mylist = []

for item in tup:
    if item % 2 != 0:
        mylist.append(item)

print(mylist)
        
    
           

        


# In[5]:


# 16 Write a python statement to find the number of items in the below dictionary
# When executed, this block should produce the output 4                                                          - 3 points

dict1 = {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan'}

print(len(dict1))


# In[7]:


# 17 Write python statements to iterate through the dictionary to print keys and their corresponding values         - 3 points
# Output of this block should be:
# car honda
# color blue
# mpg 32
# type sedan

dict1 = {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan'}

def dictiteriator(obj):
    for k,v in obj.items():
        print(k,v)
        
dictiteriator(dict1)


# In[16]:


# 18 Write python statements to replace the value of key car from honda to bmw and print the dictionary             - 3 points
# Output of this code block should be {'car':'bmw', 'color':'blue', 'mpg':32, 'type':'sedan'}

dict1 = {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan'}

dict1['car'] = 'bmw'

dict1


# In[5]:


# 19 Write a python statement to join two dictionaries
# Output of this code block should be {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan', 'price':'20k'}    - 3 points

dict1 = {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan'}
dict2 = {'price':'20k'}

dict1.update(dict2)

dict1



# In[15]:


# 20 Write a python statement to print value for the key 'color'                                                     - 3 points
# Output of this block should be 'blue'

dict1 = {'car':'honda', 'color':'blue', 'mpg':32, 'type':'sedan'}

def ditioniterator(obj):
    for v in obj.values():
        if v == 'blue':
            print(v)
        
ditioniterator(dict1)


# In[18]:


# 21 Iterate through the nested list to sort individual lists
# Output of this block should be [[4, 5, 8], [11, 13, 20]]                                                         - 4 points

lst = [[8, 4, 5], [20, 11, 13]]

for nestedlist in lst:
    nestedlist.sort()
print(lst)


# In[28]:


# 22 Iterate through the nested list to print all odd numbers
# Output of this block should be 3 5 11 13                                                                         - 5 points

lst = [[3, 4, 5], [10, 11, 13]]

for nestedlist in lst:
    for num in nestedlist:
        if num % 2 != 0:
            print(num)
       


# In[138]:


# 23 Write a function that adds a space character. The space should appear after three character so use this hint while 
# iterating through the string object. Output of this block should be 'BUS 443'
# HINT: Since strings are immutable you have to use a new string object to store the new string with a space      - 5 points

strobj = 'BUS443'


def addspace(strobj):
    result = ''
    for index in range(len(strobj)):
        if index == 3:
            result = result + " "
        result = result + strobj[index]
    
        
    
    return result
    

# Calling the function with the string object
print(addspace(strobj))


# In[85]:


# 24 Write a function that accepts a nested list and returns the nested list with every number squared
# Output of this block should be [[9,4,16], [121,81,400]]                                                           - 5 points

lst = [[3,2,4], [11,9,20]]

def squarelst(lst):
    result = []
    for i in range(len(lst)):
        temp = []
        for j in range(len(lst[i])):
            temp.append(lst[i][j]**2)
        result.append(temp) 
    return result

print(squarelst(lst))


# In[109]:


# 25 To the below function, add a try exception block that handles divide by zero error and also has a general exception block
# If divide by zero error occurs, print("Denominator is 0") for all other errors, print("Unexpected error").
# Test your code by setting denominator = 0                                                                        - 5 points

def testfunction():
    numerator = 10
    denominator = 0
    quotient = ""
    try:
        quotient = calculator(numerator,denominator,'Divide')
    except ZeroDivisionError:
        quotient = "Denominator is 0"
    except:
        print("Unexpected error")
    return quotient


print(testfunction())
    


# In[86]:


def calculator (numerator, denominator, operand):
    if operand == 'Divide':
        return numerator/denominator
    else:
        return ("Unexpected error")


# In[117]:


# 26 Given the list below, write a function to add all the elements at odd indices and append the total to the end of the list
# and return the list 
# Remember list index starts at 0
# Output of this block should be [23, 13, 65, 21, 10, 6, 45, 67, 98, 321, 6, 61, 16, 70, 559]                      - 5 points

lst = [23, 13, 65, 21, 10, 6, 45, 67, 98, 321, 6, 61, 16, 70]

def addlst(lst):
    result = []
    sum = 0
    for index in range(len(lst)):
        if index % 2 != 0:
            sum = lst[index] + sum 
        result.append(lst[index])
    result.append(sum)
    return result
    

print(addlst(lst))


# In[73]:


# 27 Write a function that accepts a dictionary as argument.
# Iterate through the dictionary to print key and value of course and number, check if place is equal to            - 10 points
# b410. If yes then change it to b411 and then print the key and value.
# Output will be 
# course bus
# number 443
# place b411

mydict = {'course': 'bus', 'number': 443, 'place':'b410'}

def iterdict(mydict):
    for k,v in mydict.items(): 
        if k == "place" and v == 'b410':
            mydict[k] = "b411"
        print(k,mydict[k])
    
        
iterdict(mydict)


# In[ ]:




