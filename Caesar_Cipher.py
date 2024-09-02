def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Add other characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher program!")
    
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Enter Q to quit): ").upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        
        if choice not in ['E', 'D']:
            print("Invalid choice. Please choose E to encrypt, D to decrypt, or Q to quit.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            print("Encrypted message: " + encrypt(message, shift))
        elif choice == 'D':
            print("Decrypted message: " + decrypt(message, shift))

if __name__ == "__main__":
    main()
