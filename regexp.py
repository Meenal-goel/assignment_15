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

#4-Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
#desired_output = 'Good advice What I would do differently if I was learning to code today'

import re
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
def cleaning_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)  # remove URLs
    tweet = re.sub('RT', '', tweet)  # remove RT
    tweet = re.sub('cc:','',tweet)   #remove cc
    tweet = re.sub('#\S+', '', tweet)  # remove hashtags
    tweet = re.sub('@\S+', '', tweet)  # remove mentions
    tweet = re.sub('\s+', ' ', tweet)  # remove extra whitespace
    tweet = re.sub('!','',tweet) #remove !
    return tweet

print(cleaning_tweet(tweet))
