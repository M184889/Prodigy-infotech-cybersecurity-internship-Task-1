# Caesar Cipher Implementation in Python
# Encrypts and Decrypts user input based on shift value

# Function to encrypt the message
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine if it's uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet using modulo
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            # Keep non-alphabetic characters (e.g. space, punctuation) unchanged
            encrypted_text += char

    return encrypted_text

# Function to decrypt the message
def decrypt(text, shift):
    # Decryption is the reverse of encryption (shift in opposite direction)
    return encrypt(text, -shift)

# Main function to run the Caesar Cipher program
def caesar_cipher():
    print("=== Caesar Cipher Program ===")

    # Ask the user for mode: Encrypt or Decrypt
    choice = input("Type 'E' for Encrypt or 'D' for Decrypt: ").strip().upper()

    # Ask the user for the message
    message = input("Enter your message: ")

    # Ask the user for the shift value
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer!")
        return

    # Perform the requested operation
    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted Message:", result)
    elif choice == 'D':
        result = decrypt(message, shift)
        print("Decrypted Message:", result)
    else:
        print("Invalid option. Please choose 'E' or 'D'.")

# Run the program
caesar_cipher()
E