#!/usr/bin/env python
# coding: utf-8

# #### KPMG Challenge - 3 
# 
# We have a nested object, we would like a function that you pass in the object and a key and get back the value.
#  
# Example Inputs
# object = {“a”:{“b”:{“c”:”d”}}}
# key = a/b/c
#  
# object = {“x”:{“y”:{“z”:”a”}}}
# key = x/y/z
# value = a

# ##### create a nested object

# In[58]:


nested_object = {"a":{"b":{"c":"d"}}}


# ##### define a function that takes in the nested object and a key to get back the value

# In[59]:


def get_value_of_nested_object(_dict, keys, default=None):
    """
    Summary : This function takes in keys and returns the value of a nested object
    Input   : Keys passed in as a list
    Output  : Value of the nested object
    Usage   : get_value_of_nested_object(<nested_object_name>, <[list_of_keys]>)
    Example : get_value_of_nested_object(nested_object, ['a','b','c'])
    Output  : 'd'
    """
    for key in keys:
        if isinstance(_dict, dict):
            _dict = _dict.get(key, default) 
        else:
            return default
    return _dict


# In[60]:


print (get_value_of_nested_object(nested_object, ['a', 'b', 'c']))


# In[61]:


def get_value_of_nested_object(_dict, keys, default=None):
    """
    Summary : This function takes in keys and returns the value of a nested object
    Input   : Keys passed in as a String separated by '/'
    Output  : Value of the nested object
    Usage   : get_value_of_nested_object(<nested_object_name>, <keys_string>)
    Example : get_value_of_nested_object(nested_object, "a/b/c")
    Output  : 'd'
    """
    keys_list = keys.split("/")
    for key in keys_list:
        if isinstance(_dict, dict):
            _dict = _dict.get(key, default) 
        else:
            return default
    return _dict


# In[62]:


print (get_value_of_nested_object(nested_object, "a/b/c"))

