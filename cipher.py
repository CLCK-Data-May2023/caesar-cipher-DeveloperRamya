# add your code here
def caesar_cipher_encrypt(text, shift):
    encrypted_sentence = ""
    for char in text:
        if char.isalpha():
            base = ord('a') 
            encrypted_char = chr((ord(char.lower()) - base + shift) % 26 + base)
            encrypted_sentence += encrypted_char
        else:
            encrypted_sentence += char.lower()
    return encrypted_sentence

def main():
    plain_text = input("Please enter a sentence: ")
    shift = 5
    encrypted_sentence = caesar_cipher_encrypt(plain_text, shift)
    print("The encryted sentence is:", encrypted_sentence)

if __name__ == "__main__":
    main()
