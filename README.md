# Challenge_two_and_three

Challenge 2:

Problem Statement:
We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to you.

Solution:
1) I've quickly created an AWS EC2 Linux Instance just to be able to test out my script.
2) Selected python as my scripting language
3) Script Details: Challenge2.py
4) Metadata of any AWS Instance can be retrieved by running the script on that particular Instance. Output will be as shown in Challenge2_Output.png

Challenge 3:
Problem Statement:
We have a nested object, we would like a function that you pass in the object and a key and get back the value.

Solution:
1) Selected python as my scripting language
2) Created two functions so that the value can be obtained even if we pass the object and keys in different ways.

Ex: get_value_of_nested_object(nested_object, ['a', 'b', 'c']) gives output d 

    get_value_of_nested_object(nested_object, "a/b/c") gives output d
