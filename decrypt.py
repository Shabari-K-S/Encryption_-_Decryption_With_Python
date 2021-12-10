message = input("Enter the message to be decrypted:")

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_\{\}+-=|[] 1234567890'

key = int(input("Enter the key :"))

decrypt = ''


for e in message:
	position = alphabet.find(e)
	newposition = (position - key) % 83
	decrypt += alphabet[newposition]
print(decrypt)