#!/usr/bin/env python
# coding: utf-8

#  Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# In[1]:


def inputs():
    for i in range(1,101):
        p = i % 3
        f = i % 5
        if (p==0 and f ==0):
            print("FizzBuzz")
        elif f == 0:
            print("Buzz")
        elif p == 0:
            print("Fizz")
        else:
            
            print(i)
inputs()        


# In[ ]:





# In[ ]:




