# add your code here
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Please enter a sentence: ")
    shift = 5
    encrypted_text = caesar_cipher_encrypt(plain_text, shift)
    print("The encryted sentence is:", encrypted_text)

if __name__ == "__main__":
    main()
