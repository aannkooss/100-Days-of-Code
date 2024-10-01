#Author: Ankush Joshi
#Date: August 12 2024
#Day 8/100 - Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'n', 'm', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

def main():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid choice, type 'encode' or 'decode'")

def encrypt(originalText, shiftAmount):
    encodedText = ""
    for letter in originalText:
        shiftedLetter = alphabet.index(letter) + shiftAmount

        shiftedLetter %= len(alphabet)
        encodedText += alphabet[shiftedLetter]

    print(f"Here is the encoded message: {encodedText}", end="")

def decrypt(shiftedText, shiftAmount):
    decodedMessage = ""
    for letter in shiftedText:
        originalLetter = alphabet.index(letter) - shiftAmount

        originalLetter %= len(alphabet)
        decodedMessage += alphabet[originalLetter]

    print(f"Here is the decoded message: {decodedMessage}", end="")

main()