# getting input as message from user.

message = input("Enter the message to be decrypted:")

# alphabets is used to compare with message to change the letter to display.

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_\{\}+-=|[] 1234567890'

key = int(input("Enter the key :"))		# key the value to change the message for alphabets

decrypt = ''		# decrypt is the variable to store the data after change

# It is a loop to change the charaters with respect to key

for e in message:
	position = alphabet.find(e)
	newposition = (position - key) % 83
	decrypt += alphabet[newposition]
print(decrypt)

# After the loop it change all the character respect to key and store the value in decrypt
