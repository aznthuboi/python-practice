string = str(input('Enter a few words: '))

def rvs(string):
    r = string.split()
    return " ".join(r[::-1])

print(rvs(string))