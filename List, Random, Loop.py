#list
colors = ['red', 'blue', 'green']
colors[0]   # zero base indexing
colors[1]
colors[2]

colors.append('purple')
colors.remove('green')
colors

colors.extend(['green', 'yellow'])
'green' in colors

colors[3]

type(colors)

#random
import random

random.randint(0,3)

colors = [random.randint(0,2)]
colors = [random.randint(0,len(colors))]

random.choice(colors)

#loop
colors = ['red','blue','green']

for color in colors:
    print('I love {}'.format(color))

range(3)

for i in range(3):
    print(i)

for i in range(5):
    print(i)

# break, pass, continue
for i in range(3):
    cmd = input('Enter command: ')
    if cmd == 'break':
        break
    elif cmd == 'pass':
        pass
        print('command is pass')
    elif cmd == 'continue':
        continue
        print('command is continue')
