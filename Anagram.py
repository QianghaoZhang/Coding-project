#!/usr/bin/env python
# coding: utf-8

# In[19]:



#Problem
#Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

#For example:

#"public relations" is an anagram of "crap built on lies."

#"clint eastwood" is an anagram of "old west action"


# In[ ]:


# My method


# In[2]:


from itertools import permutations


# In[16]:


#method 1
def anagram(s1,s2):
    s1_terms = [''.join(i) for i in permutations(s1)]
    if s2 in s1_terms:
        return True
    return False
            


# In[17]:


anagram('dog','god')


# In[ ]:


#method2


# In[4]:


def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2= s2.replace(' ','').lower()
    return sorted(s1)==sorted(s2)


# In[ ]:





# In[5]:


#method 3


# In[14]:


def anagram3(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2= s2.replace(' ','').lower()
    
    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
             count[letter]+=1
        else:
             count[letter]=1
    for letter in s2:
        if letter in count:
             count[letter]-=1
        else:
             count[letter]=1
    
    for k in count:
        if count[k]!=0:
            return False
        
    return True
            


# In[15]:


anagram3('dog','god')


# In[ ]:




