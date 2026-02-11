import re
from collections import Counter

word = "Umer $ Azmi' ? 'UA"
words = ["apple", "banana", "cherry"]
print('\nWord:', word)
sort = sorted(word.lower())                         #Sorted()
sub = re.sub(r'[^a-zA-Z0-9]','',word)   #Re.Sub()
# Reverse the entire list
words.reverse()                                     #Reverse()


print('Sorted: ',sort)
print('Subbed: ',sub)
print('Reversed: ',words)

# Reversed only the letters of the string
s = "maam took her gayat to the lake, but wow, a pup jumped in!"
words = s.split()                                   #Split
reverse_words = [w[::-1] for w in words]
print('\nReversed Words:\n',reverse_words)
print(' '.join(reverse_words))                      #Join


haystack = ['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
find_needle(haystack)