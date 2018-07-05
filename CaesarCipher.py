MAX_KEY_SIZE=25 #maximum key size


myName=''

# This input in the while loop asks the user for their name, and the user is prompted to
# enter more than 3 characters.  Afterwards, it aslo checks to make sure that the input
# contains only alphabets, no numbers or special characters.
while not myName.isalpha() or len(myName)<3: #
	myName=input('Please enter your name (use letters only and make sure it is more than 3 characters) : ')
print('Hello ' + myName.capitalize())


#This function will let the user type in if they want to encrypt or decrypt
def getMode():
	while True:
		mode=input('Do you wish to encrypt (e) or decrypt (d) your message? ').lower()
		if mode.lower() in {"e", "d"}:
			return mode
		print('Please enter "e" to encrypt or "d" to decrypt' )

# This function gets the message to encrypt or decrypt from the user and returns it
def getMessage():
	while True:
		message=input('Please enter your message: ')
		if not all (message.isdigit() or message.isspace() for message in message):
			return message
		print('Invalid input, it must contain alphabetic characters ')



# getKey() function lets us type in the key we will use to encrypt or decrypt the message
def getKey():
	key = 0
	while True:
		try:
			print('Please enter the key number, make sure to use integers from (3 - %s) ' % (MAX_KEY_SIZE))
			key=int(input())
			if (key>=3 and key<=MAX_KEY_SIZE):
				return key

		except ValueError:
			print('Please use integers only from 3 - 25')
			continue
		if (key<3 or key>MAX_KEY_SIZE):
			print ('Invalid input, please use the numbers between the range')

#This function does the encrypting and decrypting with 3 parameters: mode, message, key
#The mode sets the function to encryption mode or decryption mode.
#line 58 checks if the first letter in the mode variable is the string 'd'. If so, then the program is in decryption mode
def getTranslatedMessage(mode, message, key):
	if mode[0]=='d':
		key=-key
	translated= ''
#The isalpha() string method will return True if the string is an uppercase or lowercase letter from A to Z
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num +=key
#isupper() will return True if the string it is called on contains at least one uppercase letter
#line 68 checks if num has a value larger than the ordinal value for “Z”. If so, then subtract 26 (to go back to the beginning of the alphabet)
			if symbol.isupper():
				if num>ord('Z'):
					num -=26
				elif num < ord('A'):
					num+=26
#islower() returns True if the string it is called on contains at least one lowercase letter
			elif symbol.islower():
				if num>ord('z'):
					num -=26
				elif num<ord('a'):
					num+=26
#In decrypting mode key would be negative.
			translated+=chr(num)
		else:
			translated+=symbol
	return translated

#These three values are passed to getTranslatedMessage(), whose return value (the translated string) is printed to the user.
mode=getMode()
message=getMessage()
key=getKey()

print('Translating your message...')
print(getTranslatedMessage(mode, message, key))

print('Well Done!')
