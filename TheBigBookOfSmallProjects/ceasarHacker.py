print('Enter the encrypted Caesar cipher message to hack.')
text = input('> ').upper()

text = list(text)

for key in range(25):
    temp = text.copy()
    for i, char in enumerate(temp):
        n = ord(char)
        if n in range(65, 97):
            n = (n - key - 65) % 26
            temp[i] = chr(n + 65)

    result = ''.join(temp)
    print('Key #{}:'.format(key), result)
