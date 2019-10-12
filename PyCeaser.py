def encrypt(Message,key):
    Encrypted_Message = ""
    for i in range(len(Message)):
        character = Message[i]


        if (character.isupper()):
            Encrypted_Message += chr((ord(character) + key - 65) % 26 + 65)

        else:
            Encrypted_Message += chr((ord(character) + key - 97) % 26 + 97)
    return Encrypted_Message


def decrypt(Encrypted_Message,key):
    Decrypted_Message = ""
    for i in range(len(Encrypted_Message)):
        character = Encrypted_Message[i]


        if (character.isupper()):
            Decrypted_Message += chr(90 - (90 - (ord(character) - key)) % 26)
        else:
            Decrypted_Message += chr(122 - (122 - (ord(character) - key)) % 26)
    return Decrypted_Message


print('<---Please select one of the options given below--->\n')
Value = int(input('1 : Encryption\n2 : Decryption\n-->'))

if(Value == 1):
    Message = input("Please Enter Your MESSAGE (Plain Text) : ")
    key = int(input('Please Enter the desired SHIFT KEY : '))
    print("Encrypted Message : ", encrypt(Message, key))


elif(Value == 2):
    Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
    key = int(input('Please Enter the desired SHIFT KEY : '))
    print("Decrypted Message : ", decrypt(Message, key))

else:
    print('Please Select the Valid Option')
