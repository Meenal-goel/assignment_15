#1- Extract the user id, domain name and suffix from the following email addresses. 
#emails = "zuck26@facebook.com" "page33@google.com"
#"jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]


import re


emails = ("zuck26@facebook.com" "page33@google.com""jeff42@amazon.com")
matcher = re.findall('(\w+)@([a-z0-9]+)\.([a-z]{2,3})',emails, flags=0)#regexp for email can be found online
print(matcher)
print("\n")
print("-"*200)
print("\n")

#2-Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

import re
text = ("Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.")
matcher = re.findall(r'\bB\w+', text, flags=re.IGNORECASE)#r signifies that actual meaning of / needs to be overlooked
print(matcher)
print("\n")
print("-"*200)
print("\n")

#3-Split the following irregular sentence into words 
'''sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence"
OPTIONAL QUESTION'''

import re
sentence = "A, very very; irregular_sentence"
s =  re.sub('[;,\s_]+',' ' ,sentence)
print(s)
print("\n")
print("-"*200)
print("\n")
