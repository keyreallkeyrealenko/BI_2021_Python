print('This is a Time Converter, here you can convert between the following measurements:'
      ' \n1)seconds\n2)minutes\n3)hours\n4)days\n5)weeks\n6)years\n')

print('Enter two letters separated by "-" to convert these measurements (e.g s-c means seconds to centuries)')

# Making two lists to compare entered command with available commands
command_lst = ['s-m', 's-h', 's-d', 's-w', 's-y', 'm-h', 'm-d', 'm-w', 'm-y', 'h-d', 'h-w', 'h-y',
               'd-w', 'd-y', 'w-y']

rev_command_list = []
for i in command_lst:
    rev_command_list.append(i[::-1])

# Checking if the command is valid
n = 0
convert_command = input()
while n != 1:
    if convert_command not in command_lst and convert_command not in rev_command_list:
        print('Invalid command. Correct command should be like "m-s" where "m" – minutes to "s" – seconds')
        print("Try again: ")
        convert_command = input()
    else:
        n += 1

# Performing converting
value = 0
if convert_command[0] == 's':
    value = float(input('Enter seconds: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter seconds: '))
    if convert_command[-1] == 'm':
        ans = round(value / 60, 3)
        print(f'{value} seconds are {ans} minutes')
    elif convert_command[-1] == 'h':
        ans = round(value / 3600, 3)
        print(f'{value} seconds are {ans} hours')
    elif convert_command[-1] == 'd':
        ans = round(value / 86400, 3)
        print(f'{value} seconds are {ans} days')
    elif convert_command[-1] == 'w':
        ans = round(value / 604800, 3)
        print(f'{value} seconds are {ans} weeks')
    elif convert_command[-1] == 'y':
        ans = round(value / 31556952, 3)
        print(f'{value} seconds are {ans} years')
elif convert_command[0] == 'm':
    value = float(input('Enter minutes: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter minutes: '))
    if convert_command[-1] == 's':
        ans = value * 60
        print(f'{value} minutes are {ans} seconds')
    elif convert_command[-1] == 'h':
        ans = round(value / 60, 3)
        print(f'{value} minutes are {ans} hours')
    elif convert_command[-1] == 'd':
        ans = round(value / 1440, 3)
        print(f'{value} minutes are {ans} days')
    elif convert_command[-1] == 'w':
        ans = round(value / 10080, 3)
        print(f'{value} minutes are {ans} weeks')
    elif convert_command[-1] == 'y':
        ans = round(value / 525960, 3)
        print(f'{value} minutes are {ans} years')
elif convert_command[0] == 'h':
    value = float(input('Enter hours: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter hours: '))
    if convert_command[-1] == 's':
        ans = 3600 * value
        print(f'{value} hours are {ans} seconds')
    elif convert_command[-1] == 'm':
        ans = 60 * value
        print(f'{value} hours are {ans} minutes')
    elif convert_command[-1] == 'd':
        ans = round(value / 24, 3)
        print(f'{value} hours are {ans} days')
    elif convert_command[-1] == 'w':
        ans = round(value / (24 * 7), 3)
        print(f'{value} hours are {ans} weeks')
    elif convert_command[-1] == 'y':
        ans = round(value / 8766, 3)
        print(f'{value} hours are {ans} years')
elif convert_command[0] == 'd':
    value = float(input('Enter days: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter days: '))
    if convert_command[-1] == 's':
        ans = 86400 * value
        print(f'{value} days are {ans} seconds')
    elif convert_command[-1] == 'm':
        ans = 1440 * value
        print(f'{value} days are {ans} minutes')
    elif convert_command[-1] == 'h':
        ans = 24 * value
        print(f'{value} days are {ans} hours')
    elif convert_command[-1] == 'w':
        ans = round(value / 7, 2)
        print(f'{value} days are {ans} weeks')
    elif convert_command[-1] == 'y':
        ans = round(value / 365.25, 3)
        print(f'{value} days are {ans} years')
elif convert_command[0] == 'w':
    value = float(input('Enter weeks: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter weeks: '))
    if convert_command[-1] == 's':
        ans = 604800 * value
        print(f'{value} weeks are {ans} seconds')
    elif convert_command[-1] == 'm':
        ans = 10080 * value
        print(f'{value} weeks are {ans} minutes')
    elif convert_command[-1] == 'h':
        ans = 168 * value
        print(f'{value} weeks are {ans} hours')
    elif convert_command[-1] == 'd':
        ans = 7 * value
        print(f'{value} weeks are {ans} days')
    elif convert_command[-1] == 'y':
        ans = round(value / 52.1786, 3)
        print(f'{value} weeks are {ans} years')
elif convert_command[0] == 'y':
    value = float(input('Enter years: '))
    while value <= 0:
        print('It should be more than 0')
        value = float(input('Enter years: '))
    if convert_command[-1] == 's':
        ans = 31556952 * value
        print(f'{value} years are {ans} seconds')
    elif convert_command[-1] == 'm':
        ans = 525960 * value
        print(f'{value} years are {ans} minutes')
    elif convert_command[-1] == 'h':
        ans = 8766 * value
        print(f'{value} years are {ans} hours')
    elif convert_command[-1] == 'd':
        ans = 365.25 * value
        print(f'{value} years are {ans} days')
    elif convert_command[-1] == 'w':
        ans = 52.1786 * value
        print(f'{value} years are {ans} weeks')
