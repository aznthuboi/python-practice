# generate a password with length "passlen" with no duplicate characters in the password
import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print p

#s2
import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

# Complete use of ASCll CODE found online
import random
def pass_gen():
    chars = list(range(ord('A'), ord('Z') + 1))
    chars += list(range(ord('a'), ord('z') + 1))
    chars += list(range(ord('0'), ord('9') + 1))
    chars += list(range(ord('!'), ord('&') + 1))
    return chars

def generateKey(keyString):
    key = []
    for i in range(12):
        key.append(chr(keyString[random.randint(0, len(keyString)-1 )]) )
    return (key)

password = ''.join(generateKey(pass_gen()))
print (password)