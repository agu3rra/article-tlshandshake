message = 'Divide the army in two, advance and outflank them on the right. I will advance on the left flank from the woods getting them by surprise.'
message = message.replace(' ','')
message = message.replace(',','')
message = message.replace('.','')
shift_secret = 6
ciphered_message = ''
print(message)
for character in message:
    if character.isupper():
        ciphered_message += chr((ord(character) + shift_secret - 65) % 26 + 65)
    else:
        ciphered_message += chr((ord(character) + shift_secret - 97) % 26 + 97)
print(ciphered_message)
