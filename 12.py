#Makes new list of only first and last element
a = [5, 10, 15, 20, 25]
def list(a):
    return [a[0], a[len(a)-1]]

print(list(a))
