import optparse

root = optparse.OptionParser()

root.add_option("-o","--option",dest="opt",help="use this to encrypt(to encrypt the message use 'encrypt') or decrypt(to decrypt the message use 'decrypt') your message(use thos without singlecotes and doublecotes)")
root.add_option("-k","--key",dest="key",help="use key (only number are acceptable.)to encrypt or decrypt your message")
root.add_option("-m","--message",dest="msg",help="Enter the content to be encrypt or decrypt(write everything within doublecotes)")

(options, arguments) = root.parse_args()


if (options.opt=="encrypt"):
    message = options.msg
    alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm 1234567890'
    key = options.key
    pswd = int(key)
    encrypt = ''		
    
    for e in message:
        position = alphabet.find(e)
        newposition=(position + pswd)%63
        encrypt += alphabet[newposition]
    print("The Message after encryption :",encrypt)

elif(options.opt=="decrypt"):
    message = options.msg
    alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm 1234567890'
    key = options.key
    pswd = int(key)
    decrypt = ''
    for e in message:
        position = alphabet.find(e)
        newposition=(position-pswd)%63
        decrypt += alphabet[newposition]
    print("The message after decryption :",decrypt)
else:
    print("Invalid option.")