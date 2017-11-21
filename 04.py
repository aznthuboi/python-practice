num = int(input("Enter a number: "))
listRange = list(range(1,num+1))
divisorList = []

for i in listRange:
	if num % i == 0:
		divisorList.append(i)

print(divisorList)