import json

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#import content from json file
with open("input.json", "r") as file:
    input_from_file = json.load(file)

direction = input_from_file['direction']
text = input_from_file['text']
shift = input_from_file['shift']

#create dictionary to be inserted into the output file
out_dict = {}

out_dict['text'] = text
out_dict['direction'] = direction
out_dict['shift'] = shift

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
    my_dict = {}
    for letter in input_text:
        if letter == ' ':
            encrypted_text.append(' ')
        else:
            possition = alphabet.index(letter) - shift_amount
            if possition < 0:
                possition += 26
            encrypted_text.append(alphabet[possition])
    
    return ''.join(encrypted_text)
    
#decide to encrypt or decrypt message
match direction:
    case 'encode':
        out_dict['new_text'] = encrypt(text, shift)    
    case 'decode':
        out_dict['new_text'] = decrypt(text, shift)
    case _:
        print('Wrong command!')

#write the output dictionary into the output file        
with open('output.json', 'w') as output:
    json.dump(out_dict, output, indent=4)