import enchant


dipper = "abcdefghijklmnopqrstuvwxyz"
d = enchant.Dict("en_US")
decrypted_msg = []
score = []


def get_keys(message):

    for key in range(0, 27):
        mabel = decrypt2(key)
        zipping(message, mabel)



def encrypt(Message,key):
    Encrypted_Message = ""
    Message = Message.lower()
    for i in range(len(Message)):
        character = Message[i]
        Encrypted_Message += chr((ord(character) + key - 97) % 26 + 97)
    return Encrypted_Message


def decrypt1(Encrypted_Message,key):
    Decrypted_Message = ""
    for i in range(len(Encrypted_Message)):
        character = Encrypted_Message[i]
        Decrypted_Message += chr(122 - (122 - (ord(character) - key)) % 26)
    return Decrypted_Message


def decrypt2(shift):
    shifted_alphabet_lines = ""
    shift %= 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        character = alphabet[i]
        shifted_alphabet_lines += chr(122 - (122 - (ord(character) - shift)) % 26)
    return shifted_alphabet_lines



def zipping(message, mabel):
    word = message.translate({ord(x): y for (x, y) in zip(dipper, mabel)})
    decrypted_msg.append(word)
    score_check(word)


def score_check(line):
    points = 0
    words = line.split()
    for word in words:
        if d.check(word):
            points += 1
        else:
            pass
    score.append(points)


def show_final_guess(input_word):
    total_words = len(input_word.split())
    for index in range(0,len(decrypted_msg)):
        probability = score[index]/total_words * 100
        if probability == 100 :
            print("Decrypted Message : " + decrypted_msg[index])


if __name__ == "__main__":

    print('<---Please select one of the options given below--->\n')
    Value = int(input('1 : Encryption\n2 : Decryption\n-->'))

    if (Value == 1):
        Message = input("Please Enter Your MESSAGE (Plain Text) : ")
        key = int(input('Please Enter the desired SHIFT KEY : '))
        print("Encrypted Message : ", encrypt(Message, key))


    elif (Value == 2):
        print('<---Please select one of the options given below--->\n')
        Value = int(input("1 : If you know the key\n2 : If you don't know the key\n-->"))
        if Value == 1:
            z = []
            Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
            Message = Message.lower()
            Message = Message.split()
            key = int(input('Please Enter the desired SHIFT KEY : '))
            for m in Message:
                x = decrypt1(m, key)
                z.append(x)
            l = " ".join(z)
            print("Decrypted Message : ", l)

        elif Value == 2:
            Message = input("Please Enter Your MESSAGE (Cipher Text) : ")
            Message = Message.lower()
            get_keys(Message)
            print("\nSorry(if and only if the list is too long) :\n")
            show_final_guess(Message)

        else:
            print('Please Select the valid Option')
    else:
        print('Please Select the Valid Option')
