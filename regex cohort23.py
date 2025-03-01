# REGULAR EXPRESSION == REGEX
# INTRODUCTION TO REGEX
# SIMPLE CHARACTER MATCHES
# CHARACTER CLASSES
# SPECIAL CHARACTERS
# QUANTIFIERS
# SUBSTITUTING
# COMPLING REGULAR EXPRESSION
# SPLIT FUNCTION USING REGEX


# COREY SCHAFER

# import re
# 2 - SIMPLE CHARACTER MATCHES
import re

# text = 'cat bat mat rat mat mat'
# pattern = 'mat'
# re.findall('the patter would go here', 'the text would go here'
# output = re.findall(pattern,text)

# print(len(output))

# 3 - CHARACTER CLASSES

# text = 'we have 3 Apples and 14 oranges in 1343 avenue which is priced for $40.'
# pattern = r'[\w]+' #trying to get matches for letters both uppercase and lowercase and digits
# output = re.findall(pattern,text)
# print(output)

# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[a-zA-Z\d]+'  #trying to get matches for digits for letters both uppercase and lowercase and digits
# output = re.findall(pattern,text)
# print(output)


# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[\s]'  #trying to get matches for spaces
# output = re.findall(pattern,text)
# print(output)


# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern = r'[^a-z]+'  #trying to get matches for spaces
# output = re.findall(pattern,text)
# print(output)


# text = 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
# pattern = r'[\$\.]'   #extract the dollar sign
# output = re.findall(pattern,text)
# print(output)

# text = ('We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40')
        # '#extract the dollar sign)
# output = re.findall(pattern,text)
# print(text)

# 4 - SPECIAL CHARACTERS

text = 'hello, world, hallo heeello'
pattern = r'h.llo'  #trying to extract word that starts with 'h' but ends with 'llo' but has one letter
# output = re.findall(pattern,text)
# print(output)
# text = 'hello, world, hallo heeello'
# pattern = r'h.*llo'  #trying to extract a word
# output = re.findall(pattern,text)
# print(output)


# text = 'hello, world hallo heeello'
# pattern = r'h.*?llo'  #trying to extract a word
# output = re.findall(pattern,text)
# print(output)

# SUBSTITUTING


# text = 'Lawal and Muhammad are friends'
# pattern = 'friends'

# re.sub('the pattern that we are trying to substitute', 'the replacement word' 'text')
# output = re.sub(pattern, 'enemies', text)
# print(output)


# SPLIT FUNCTION USING REGEX

# text = 'My name is Mubaraq, I am 40 years old'
# NORMAL SPLIT FUNCTION
# print(text.split())
# print(text.split(' '))
# print(text.split('a'))
# USING REGEX TO SPLIT
# pattern = r'\s+'
# print(re.split(pattern,text))