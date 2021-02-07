#a program writing 0, n including n

n = int(input("Please enter a number: "))
x = range(0, n+1)
for i in x:
    if (i%2) == 0:
    	print(i)
