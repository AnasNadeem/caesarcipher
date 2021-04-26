def ceaser_cipher(enc, message, shift):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v','w', 'x', 'y', 'z']
    cipher = ''
    if enc=='encrypt':
        for msg in message:
            letter_position = letters.index(msg)
            cipher_position = letter_position + shift
            if cipher_position >= 26:
                new_position = cipher_position % 26
                cipher += letters[new_position]
            else:
                cipher += letters[cipher_position]
        print(f'Your encrypted message is: {cipher}')
    elif enc=='decrypt':
        for msg in message:
            letter_position = letters.index(msg)
            cipher_position = letter_position - shift
            if cipher_position >= 26:
                new_position = cipher_position % 26
                cipher += letters[new_position]
            else:
                cipher += letters[cipher_position]
        print(f'Your decrypted message is: {cipher}')
    else:
        'Give a correct input.'


wanna_continue = True
while wanna_continue:
    enc_or_dec = input('Encrypt or Decrypt\t').lower()
    message = input('Message:\n')
    shift = int(input('Shift:\t'))
    ceaser_cipher(enc_or_dec, message, shift)
    ask_continuation = input('Wanna continue:\n').lower()
    if ask_continuation=='no':
        wanna_continue=False
        print('Thanks for using the program')
    elif ask_continuation=='yes':
        enc_or_dec = input('Encrypt or Decrypt\t').lower()
        message = input('Message:\n')
        shift = int(input('Shift:\t'))
        ceaser_cipher(enc_or_dec, message, shift)
    else:
        print('Please select correct input')

