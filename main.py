cipher_format = 'abcdefghijklmnopqrstuvwxyz'
input_cipher = 'zyxwvutsrqponmljkihgfedcba'

input_callsign = input('Enter callsign: ')

deciphered_callsign = ''

for letter in input_callsign:
    index = input_cipher.index(letter.lower())
    deciphered_letter = cipher_format[index]
    deciphered_callsign += deciphered_letter

print(deciphered_callsign)
