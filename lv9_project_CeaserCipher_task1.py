alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# encrypt the given message
def encrypt(input_text, shift_amount):
    encrypted_text = []
    for letter in input_text:
        if letter == ' ':
            encrypted_text.append(' ')
        else:
            possition = alphabet.index(letter) + shift_amount
            if possition > 25:
                possition -= 26
            encrypted_text.append(alphabet[possition])
    
    return ''.join(encrypted_text)

#decrypt the given message
def decrypt(input_text, shift_amount):
    encrypted_text = []
    for letter in input_text:
        if letter == ' ':
            encrypted_text.append(' ')
        else:
            possition = alphabet.index(letter) - shift_amount
            if possition < 0:
                possition += 25
            encrypted_text.append(alphabet[possition])
    
    return ''.join(encrypted_text)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

#print out the encrypted or decrypted message
    #if direction is 'encode'
        #call encrypt()
    #if direction is 'decode'
        #call decrypt()
match direction:
    case 'encode':
        print(encrypt(text, shift))
    case 'decode':
        print(decrypt(text, shift))       
    case _:
        print('Wrong command!')           