import re

print('Igpay Atinlay (Pig Latin)')

print('Enter your message')
message = input('> ')

words = message.split(' ')

for index, word in enumerate(words):
    firstLetter = re.search(r'[a-zA-Z]', word).span()[0]
    lastLetter = len(word) - 1 - re.search(r'[a-zA-Z]', word[::-1]).span()[0]

    if word[firstLetter] in list('aeouiy'):
        words[index] = word[:lastLetter+1] + 'yay' + word[lastLetter+1:]

    else:
        words[index] = word[:firstLetter] + word[firstLetter+1:lastLetter+1] + word[firstLetter] + 'ay' + word[lastLetter+1:]

print(' '.join(words))