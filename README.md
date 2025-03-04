# Pretty Good Privacy Encryptor / Decryptor
 A program for encrypting and decripting messages using PGP


# PGP Encryption Program - README

## Overview

This project is a simple PGP (Pretty Good Privacy) tool for encrypting and decrypting messages. Users can input a message and choose to either encrypt or decrypt it. The program is designed to work across multiple computers for secure communication.

## Features

- **Encrypt Messages**: Converts plain text into encrypted text using a public key.
- **Decrypt Messages**: Converts encrypted text back to plain text using a private key.
- **Simple Interface**: A minimal UI for inputting and displaying messages.
- **Cross-Device Compatibility**: Encrypted messages can be decrypted on another machine with the correct key.

## Requirements

### **Programming Language & Libraries**

- **Python (Recommended Version: 3.x)**
- **Libraries:**
  - `gnupg` (Python GnuPG wrapper)
  - `tkinter` (For a simple GUI, optional)
  - `PyQt` (For an advanced GUI, optional)



## How It Works

### **Encrypting a Message**

1. User inputs a message.
2. Program encrypts it using a specified public key.
3. Encrypted message can be shared securely.

### **Decrypting a Message**

1. User inputs an encrypted message.
2. Program decrypts it using the corresponding private key.
3. Decrypted message is displayed to the user.

## Expected Workflow

1. **User generates or imports a PGP key pair (public & private).**
2. **User encrypts a message using a recipient’s public key.**
3. **User shares the encrypted message.**
4. **Recipient decrypts it using their private key.**

## Notes

- **Private keys should always remain confidential.**
- **Ensure that public keys are properly exchanged before encryption.**
- **The program is designed to be user-friendly for both beginners and experienced users.**
- **Future improvements:** Potential support for encrypting and decrypting files.

## Next Steps

- Implement encryption and decryption functions.
- Develop a simple UI prototype.
- Test usability and security measures.

If you have any questions, feel free to reach out!

