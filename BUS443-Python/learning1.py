#!/usr/bin/env python
# coding: utf-8

# ## Midterm: Total points 100
# 
# For this midterm exam please write code in Python for the following questions. All functions should have generic exception handling blocks.

# In[63]:


# 1 (20 points) Write a python function that accepts a string as a positional argument, and for every NON Vowel character
# in the string, duplicate the character. Finally print the new string. 

# Example 1:
# Input: “apple”
# Output: “apppplle”

# Example 2:
# Input: “beast”
# Output: “bbeasstt”

# Example 3:
# Input: “try”
# Output: “ttrryy”

#def strformat(strobj):
 #   vowels = "AEIOUaeiou"
  #  new_string = ""
  #  for char in strobj:
 #       vowel = 0
  #      for char2 in vowels:
   #         if char == char2:
  #              vowel = 1
  #              break
  #      if vowel == 0:
  #          new_string += char + char
   #     else:
   #         new_string += char
   # return new_string

#strformat("apple")

def strformat(strobj):
    vowels = "aeiouAEIOU"
    new_strobj = ""
    for char in strobj:
        if char not in vowels:
            new_strobj += char * 2
        else:
            new_strobj += char
    return new_strobj

strformat("apple")


# In[68]:


# 2 (20 points) Write a python function that accepts the below list as a positional argument. The list contains dictionaries 
# (transactions) as items. Iterate through this list and for each transaction calculate total cost. Finally sum all costs  
# to get the total bill amount. Print this value as output.
# Output: 77.05

transactions = [{'item':'book', 'qty':2, 'price per item':22.50}, {'item':'pen', 'qty':12, 'price per item':1.50}, 
                {'item':'pencil', 'qty':15, 'price per item':0.75}, {'item':'glue', 'qty':1, 'price per item':2.80}]

def totalvalue(transactions):
    temp = 0
    for obj in transactions:
        temp += obj['qty'] * obj['price per item']       
    return temp
temp = final_bill
print(final_bill)


# In[107]:


# 3 (20 points) Write a python function that accepts the below dictionary as a positional argument. Iterate through this 
# dictionary and create a list. The list should contain, all the names of the books whose type = ‘paperback’ and in the 
# last index, append the sum of prices of all paperback books. Return the list.
# Output = ['Da Vinci Code', 'The Client', 'Curtain', 43.22]

book = {'Rowling':{'name':'Harry Potter', 'type':'ebook', 'price':16.87},
 'Brown':{'name':'Da Vinci Code', 'type':'Paperback','price':17.35},
 'Grisham':{'name':'The Client', 'type':'Paperback', 'price':12.39},
 'Child':{'name':'Jack Reacher', 'type':'Hardcover', 'price':18.19},
 'Christie':{'name':'Curtain', 'type':'Paperback', 'price':13.48}
 }

def iterbook(book): 
    books = []
    total_price = 0
    for item in book.values():
        if item['type'] == 'Paperback':
            books.append(item['name'])
            total_price += item['price']
    books.append(total_price)
    return books
print(iterbook(book))


# In[85]:


# 4 (20 points) Write a python function that accepts the below nested list as an argument. Iterate through the list 
# and create a new list that contains only the unique strings in the lists. Return the list. The output in this case
# will be: ['orange','peach','mango','pear','lemon']
# Because each string/fruit appears only once in the list of lists. If there are no unique strings then an 
# empty list should be returned.

lst = [['apple','orange','banana'],['peach','mango','apple'],['banana','pear','lemon','apple']]

def listunique(lst):
    newuniquelist = []
    count = {}
    for item in lst:
        for subitem in item:
            if subitem not in count:
                count[subitem] = 1
            else:
                count[subitem] += 1
    for k,v in count.items():
        if v == 1:
            newuniquelist.append(k)
            
    return newuniquelist
            
print(listunique(lst))


# In[114]:


# 5 (20 points) Write a python function that accepts a string object and counts the number of vowels in the string object
#
# Example 1: 
# Input: apple
# Output: 
# a 1
# e 1

# Example 2:
# Input: business
# Output:
# e 1
# i 1
# u 1

#Example 3
# Input: character
# Output:
# a 2
# e 1

strobj = "apple"

def countvowels(strobj):
    Vowels = 'AEIOUaeiou'
    count = 0
    for char in strobj:
        if char in Vowels:
            count += 1
    return count
print(countvowels(strobj))
            

#countvowels(strobj)


# In[ ]:





# In[ ]:




