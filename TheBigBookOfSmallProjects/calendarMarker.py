import datetime as dt
import calendar as cl

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

print('Enter the year for the calendar:')
while True:
        year = input('> ')
        if year.isdecimal():
            year = int(year)
            break

print('Enter the month for the calendar, 1-12:')
while True:
        month = input('> ')
        if month.isdecimal() and 1 <= int(month) <= 12:
            month =  int(month)
            break

def printCalendar(year, month):
    output = '\n{} {}\n'.format(cl.month_name[month].upper(), year)
    
    output += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..' + '\n'

    spaceLen = len('----------')
    weekSep = ('-'*spaceLen).join(['+'] * 8) + '\n'
    
    weekFiller = (' '*spaceLen).join('|' * 8) + '\n'

    currDate = dt.date(year, month, 1)
    while currDate.weekday() != 6:
        currDate -= dt.timedelta(days=1)

    output += weekSep
    
    while True:
        for _ in range(7):
            date = currDate.day
            
            currDate += dt.timedelta(days=1)

            output += '|{}'.format(str(date).rjust(2, ' ').ljust(spaceLen, ' '))

        output += '|\n'

        for _ in range(3):
            output += weekFiller

        output += weekSep

        if currDate.month != month:
             break

    return (output)

calendar = printCalendar(year, month)
print(calendar)

#fileName = 'calendar_{}_{}.txt'.format(year, month)

#with open(fileName, 'w') as file:
#    file.write(calendar)

#print('Saved to {}'.format(fileName))
    