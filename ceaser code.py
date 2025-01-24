alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
def ceasor(orignal_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for i in orignal_text:
        if i not in alphabet:
            cipher_text += i
        else:


            shifted_position = alphabet.index(i) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d text: {cipher_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt \n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type the the shift no: \n"))
    ceasor(text, shift, direction)

    restart = input("Type 'yes' if you want to go again.otherwise,type 'no'\n.").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
