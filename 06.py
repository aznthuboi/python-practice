string = input('Enter word: ')
string = str(string)
r_String = string[::-1] #[::-1] used for reversal 
print(r_String)

if string == r_String:
	print('This word is a palindrome')
else:
	print('This word is not a palindrome')