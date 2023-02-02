
#write
with open('todolist.txt','a') as file:
    file.write("abc")


file = open('todolist.txt', 'a')
file.write("abc")
file.close()

#read
file = open('todolist.txt','r')
file = open('/Users/madlennqu/PycharmProjects/intropython/New/todolist.txt','r')



file.readline()
file.seek(0)
for line in file:
    print(line,end='')


for index, line in enumerate(file,start=1):
   print('{}) {}'.format(index,line), end='')

file.close()


with open('todolist.txt','r') as file:
    for index, line in enumerate(file, start=1):
        print('{}) {}'.format(index, line), end='')

