import random
a = random.sample(range(10),10)
b = random.sample(range(10),10)
print(a,'\n',b)
print(set(a) & set(b))
