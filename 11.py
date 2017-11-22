#Assumes that number is grater than 2
def get_number():
    return int(input(" Pick a Number: "))

num = get_number()
a = 2

while num > a:
    if num % a == 0 and a != num:
        print('number is not prime')
        break
    elif num < a:
        print('Pick another number')
        print(get_number())
    else:
        print('this is a prime number')
        break

   
#Accounts for numbers less than 2   
def get_number():
    return int(input(" Pick a Number: "))

num = get_number()

def check_prime(n):
    n = abs(int(n))
    if n < 2:
        return False    
    if n == 2:  
        return True
    if not n and 1:
        return False
    else:
        for x in range(3,int(n** 0.5)+1,2):
            if n % x == 0:
                return False
        return True

print(check_prime(num))