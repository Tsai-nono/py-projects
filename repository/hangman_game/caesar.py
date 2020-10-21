"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Function:   Encrypt the original message using the caesar
                cipher system, and output the encrypted message.
    Principle:  Create a list of encrypted letters first,
                and then correspond to the letters one by
                one to complete the encrypted message.
    """

    while True:
        secret = int(input('Secret number: '))
        if secret > 0:
            break
        else:
            print('<Error: Need to enter a positive integer.>')

    encryption = input("What's the ciphered string? ")
    print('The deciphered string is: ' + caesar_cipher(ALPHABET, (secret % len(ALPHABET)), encryption))


def caesar_cipher(alphabet, secret, encryption):
    '''
    Function: Import original message, output encrypted message.
    :param alphabet: str,Letter list
    :param secret: int,Encryption factor.
    :param encryption: str,Letter list (encryption)
    :return: str,Encrypted message.
    '''
    old_alphabet = alphabet.upper()
    keyword = encryption.upper()
    new_encryption = ''

    new_alphabet = old_alphabet[len(old_alphabet)-secret:] + old_alphabet[:len(old_alphabet)-secret]

    for i in keyword:
        if new_alphabet.find(i) != -1:
            new_encryption += old_alphabet[new_alphabet.find(i)]
        else:
            new_encryption += i

    return new_encryption


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
