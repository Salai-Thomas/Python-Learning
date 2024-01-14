alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 
            'c', 'd', 'e', 'f', 'g','h', 'i',
            'j', 'k', 'l', 'm', 'n','o', 'p',
            'q', 'r', 's', 't', 'u','v', 'w',
            'x', 'y', 'z']

direction = input("Choose encode or decode : ")
text = input("Enter the message : ")
shift = int(input("Enter the shift number : "))

def encode(text,shift):
    final_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            final_text += alphabet[new_position] 
        else:
            final_text += char

    print(f"Encode message is {final_text}")

def decode(text,shift):
    final_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"Decode Message is : {final_text}")

if text == "encode":
    encode(text,shift)
else:
    decode(text,shift)


