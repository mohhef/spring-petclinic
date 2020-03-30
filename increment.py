file = open('counter.txt', 'r')
number = file.read()
convertToInto = int(number)

file = open('counter.txt', 'w')
number=convertToInto+1
file.write(str(number))
print(number)