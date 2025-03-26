import tkinter
import PyQt6
import gnupg
import os
import encryption_functions
import argparse

# From gnupg documentation: GnuPG works on the basis of a “home directory” which is used to store public and private keyring files as well as a trust database.
# You need to identify in advance which directory on the end-user system will be used as the home directory,
# as you will need to pass this information to gnupg

# Our default for now will be C:\Users\GNUKeyring TODO: ensure this isn't static?
# TODO

gpg = gnupg.GPG()
gpg.encoding = "utf-8"

# TODO: import both private and public keys

option = "none"

while option != "end":

    option = input(
        "Please enter a key to perform the following actions: \n \n"
        + "l: list the current keyring \n"
        + "c: create a new key \n"
        + "e: encrypt a message \n"
        + "ex: export a key \n"
        + "in: import a key \n"
        + "d: decrypt a message \n"
        + "end: terminate the program. \n"
    )

    if option == "l":
        encryption_functions.list_keys(gpg)
        print("\n")
    elif option == "c":
        encryption_functions.make_user_key(gpg)
        print("\n")
    elif option == "e":
        encryption_functions.encrypt_message(gpg)
        print("\n")
    elif option == "ex":
        encryption_functions.export_key(gpg)
        print("\n")
    elif option == "im":
        
        
        with open(r"C:\Users\Darkm\GPGInfo\key_export.asc","r") as file:
            key_data = file.read()
        
        
        with open(r"C:\Users\Darkm\GPGInfo\secret_key_to_export.asc","r") as file:
            private_key_data = file.read()
        
        
        encryption_functions.import_key(gpg, key_data,private_key_data)
        print("\n")
    elif option == "d":

        with open(r"C:\Users\Darkm\GPGInfo\message_to_decrypt.asc", "r") as file:
            message_to_decrypt = file.read()
        encryption_functions.decrypt_message(gpg, message_to_decrypt)
        print("\n")
        
