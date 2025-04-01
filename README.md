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

This software requires that Gnupg is installed on your system and that Gnupg is installed in Python as well.
For Windows, Gpg4Win is used and includes key management software Kleopatra.

Gpg4Win can be found here: https://www.gpg4win.org/

Additional instructions for installation on your Operating System can be found here: https://gnupg.org/download/index.html

Installing Gnupg within Python is done with the following command:
pip install python-gnupg

After installing these programs the software should run.

Kleopatra can be used in addition to this software to manage keys.

## Passphrases

All passphrases for created keys should be saved somewhere secure as they cannot be recovered if lost!

## Exported Keys and Messages

Public keys as well as encrypted messages are saved to the .asc files in the GPGInfo folder.

Messages or keys should be saved elsewhere since the file is overwritten when exporting a new key or encrypting a new message.

Imported keys need to be certified using a key already present in the keyring before they can be used.
This is done by selecting the uncertified key in Kleopatra, right clicking, and selecting certify key.
Another key that is certified must be selected and the password of that key entered to complete certification.

Kleopatra can be used to import keys from the aforementioned files as well.

The passphrase used to decrypt a message is the passphrase used when creating a key.


## Functions

When starting the program the user will be prompted to enter a letter to perform a specific function.

These are the following:

l:Lists all of the keys in the current gnu keyring.

c:Prompts the user to enter information to create a new public and private key.

e:Prompts the user to select the index of the recipient of a message they want encrypted.
Text from the "txt_for_decryption" file can be used, or a message may be manually entered.

ex:Exports a public key from the selected index. This should be shared with other users for sharing of encrypted messages.

Keys are saved in the key_export.asc file in the GPGInfo folder. They should be copied elsewhere as running the function again overwrites these files.

im:Imports a key into the keyring if they exist. Uses the key_export file in the GPGInfo folder.

Keys imported in this way need to be certified with Kleopatra for security purposes. instructions for this can be found above. 

d:Prompts the user to decrypt a message using the password of the key that was used to encrypt it.

Gives a no key error if the password entered is incorrect. Otherwise displays the message that was decrypted in the terminal.

Passwords to decrypt only need to be used once, as long as the key used is still in the keyring.

end:Terminates the program.


## Running from the windows terminal

The program can be run via an IDE like VSCode or opened in the terminal provided python is installed within Windows.

This can be done by right clicking and selecting the 'open in terminal' option while in the root folder of the software then entering the following command: python main.py



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
2. **User imports  and certifies the public key of the intended recipient using Kleopatra**
3. **User encrypts a message using a recipient’s public key.**
3. **User shares the encrypted message.**
4. **Recipient decrypts it using their private key's passhprase.**

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

