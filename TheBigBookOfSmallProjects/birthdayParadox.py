import datetime as dt, random

def getBirthdays(noOfBirthday):
    birthdays = []
    startDate = dt.date(2024, 1, 1)
    
    for _ in range(noOfBirthday):
        birthday = startDate + dt.timedelta(random.randint(0, 364))
        birthdays.append(birthday)

    return birthdays

def isMatch(birthdays):    
    if len(set(birthdays)) == len(birthdays):
        return None
    else: 
        count = {}
        for i in birthdays:
            count[i] = count.get(i, 0) + 1

        match = {key: value for key, value in count.items() if value != 1}
        
        return match
        

while True:
    print('How many people should I generate? (Max 100)')
    respond = input('> ')
    if respond.isdecimal() and (0 < int(respond) <= 100):
        noOfBirthday = int(respond)
        break

print(f'\nHere are {noOfBirthday} birthdays:\n')

birthdays = getBirthdays(noOfBirthday)
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

birthdaysString = []
for date in birthdays:
    month = MONTHS[date.month-1]
    day = date.day

    birthdaysString.append(f'{month} {day}')

print(', '.join(birthdaysString))

match = isMatch(birthdays)

if match is None:
    print('There are no matching birthdays.')
else:
    print('\nIn this simulation, multiple people have a birthday on ', end='')

    matches = []
    for date in match:
        matches.append(f'{MONTHS[date.month-1]} {date.day}')
    
    print(f'{", ".join(matches)}')

print(f'\nGenerating {noOfBirthday} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

timeMatch = 0

for i in range(100000):
    if i % 10000 == 0:
        print(f'{i} simulations run...')

    birthdays = getBirthdays(noOfBirthday)
    if isMatch(birthdays) != None:
        timeMatch += 1

print(f'\nOut of 100,000 simulations of {noOfBirthday} people, there was a matching birthday in that group {timeMatch} times.\nThis means that {noOfBirthday} people have a {round(timeMatch/100000*100, 4)}% chance of having a matching birthday in their group.\nThat\'s probably more than you would think!')