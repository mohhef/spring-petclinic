file = open('hello.txt', 'r')
number = file.read()
convertToInto = int(number)

file = open('hello.txt', 'w')
number=convertToInto+1
file.write(str(number))
print(number)