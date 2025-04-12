import pyperclip

print('Do you want to (e)ncrypt or (d)ecrypt?')
while True:
    action = input('> ').lower()
    if action in ('e', 'd'):
        break

print('Please enter the key (0 to 26) to use.')
while True:
    key = input('> ')
    if key.isdecimal() and 0 <= int(key) <= 25:
        key = int(key)
        break

print('Enter the message to {}.'.format('encrypt' if action == 'e' else 'decrypt'))
text = input('> ').upper()
text = list(text)

for i, char in enumerate(text):
    if ord(char) in range(65, 97):
        if action == 'e':
            n = ord(char) + key - 65
        else:
            n = ord(char) - key - 65

        n = n % 26
        text[i] = chr(n + 65)

result = ''.join(text)
print(result)

try:
    pyperclip.copy(result)
    print('Full {} text copied to clipboard.'.format('encrypted' if action == 'e' else 'decrypted'))
except pyperclip.PyperclipException as e:
    pass