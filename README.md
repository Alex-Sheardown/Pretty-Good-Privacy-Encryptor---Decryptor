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

This software requires that Gnupg is installed.
It is reccomended that Kleopatra is installed as well.
For Windows Gnupg and Kleopatra can be installed via GPG4Win.

Gpg4Win can be found here: https://www.gpg4win.org/

Additionally, it might be required to install Gnupg in python with the following command:
pip install python-gnupg

After installing these programs the software should run.

Kleopatra can be used in addition to this software to manage keys.

## Passphrases

All passphrases for created keys should be saved somewhere secure as they cannot be recovered if lost!

## Exported Keys and Messages

Public and private keys as well as encrypted messages are saved to the .asc files in the GPGInfo folder.

Private keys require a passcode to export while public keys do not.

Messages or keys should be saved elsewhere since the file is overwritten when exporting a new key or encrypting a new message.

Imported keys need to be certified using a key already present in the keyring before they can be used.
This is done by selecting the uncertified key in Kleopatra, right clicking, and selecting certify key.
Another key that is certified must be selected and the password of that key entered to complete certification.

Kleopatra can be used to import keys from the aforementioned files as well.

The passphrase used to decrypt a message is the passphrase used when creating a key.



### **Programming Language & Libraries**

- **Python (Recommended Version: 3.x)**
- **Libraries:**
  - `gnupg` (Python GnuPG wrapper)



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

