# getting input as message from user.

message = input("Enter the message to be encrypted:")

# alphabets is used to compare with message to change the letter to display.

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_\{\}+-=|[] 1234567890'

key = int(input("Enter the Password to encrypt your message:"))   		# key the value to change the message for alphabets

encrypt = ''		# encrypt is the variable to store the data after change

# It is a loop to change the charaters with respect to key.

for e in message:
	position = alphabet.find(e)
	newposition = (position + key) % 83
	encrypt += alphabet[newposition]
print(encrypt)

# After the loop it change all the character respect to key and store the value in encrypt
