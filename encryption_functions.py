import getpass 

# From gnupg documentation: GnuPG works on the basis of a “home directory” which is used to store public and private keyring files as well as a trust database.
# You need to identify in advance which directory on the end-user system will be used as the home directory,
# as you will need to pass this information to gnupg


# encrypts a message using the key from the selected index in the keyring.
# displays the key as text for copying to a text document.
def encrypt_message(myGnu):
    # list the keys in the keyring.
    list_keys(myGnu)

    public_keys = myGnu.list_keys()

    selected_index = (
        int(input("Please enter the index of the key for the intended recipient: "))
        - 1
    )

    selected_key = public_keys[selected_index]
    selected_fingerprint = selected_key["fingerprint"]
    
    
    encrypt_a_file = input("Would you like to encrypt a text file or input a message to encrypt? y/n: " )
    
    if(encrypt_a_file =="y"):
        with open(r"GPGInfo\txt_for_encryption.txt",'r') as file:
            phrase_to_encrypt = file.read()
    else:

        phrase_to_encrypt = input("Enter a message you want to encrypt: ")

    encryptedData = myGnu.encrypt(
        phrase_to_encrypt,
        recipients=selected_fingerprint,
    )

    if encryptedData.ok:
        print(
            "Encryption successful. \n"
        )
        
        with open(r"GPGInfo\message_to_decrypt.asc",'w') as file:
            file.write(str(encryptedData))
    else:
        print("Encryption Failed: ")
        print(encryptedData.status)


# create a user key with username, email, a passphrase
def make_user_key(myGnu):

    name = input("Enter a username: ")
    email = input("Enter your email address: ")
    
    
    passphrase = getpass.getpass(prompt="Please enter a passphrase for your private key: ")

    inputData = myGnu.gen_key_input(
        key_type="RSA",
        key_length="1024",
        name_email=email,
        name_real=name,
        passphrase=passphrase,
    )
    try:

        myGnu.gen_key(inputData)
        print("Key creation successful. \n")

    except Exception as e:
        print(e)


# list public keys for selection
def list_keys(myGnu):

    iterable = 1
    keys = myGnu.list_keys()

    print("Public Key IDs: \n")
    for key in keys:
        print(f" {iterable} User: {key['uids'][0]}")
        iterable += 1
    


# Decrypts a given string with a passphrase
# myGnu: gpg object containing a keyring of gnu keys.
# encryptedMessage: String of an encrypted message around 1024 characters long.
# requires the public key to be present in the keyring.
def decrypt_message(myGnu, encryptedMessage):

    passphrase = getpass.getpass(prompt="Please enter your key's password to encrypt the message: ")

    decrypted_message = myGnu.decrypt(encryptedMessage, passphrase=passphrase)

    if decrypted_message.ok:
        print("Decryption was successful, here is the message: ")
        my_message = decrypted_message.data.decode("utf-8")
        print("\n")
        print(my_message)
        return

    else:
        print("Decryption has failed:", decrypted_message.status)
        print("More details:", decrypted_message.stderr)
        return None


#exports a public key to be shared.
def export_key(myGnu):

    list_keys(myGnu)
    keys = myGnu.list_keys()

    selected_index = int(input("Enter the index of the key you want to export: ")) - 1

    if selected_index < 0 or selected_index >= len(keys):
        print("Please enter an index that is valid.")
        return

    selected_key = keys[selected_index]

    selected_key_id = selected_key["keyid"]

    public_key = myGnu.export_keys(selected_key_id)
    


#adds the specified key into the keyring.
def import_key(myGnu, keyData):

    import_result = myGnu.import_keys(keyData)

    if import_result == 0:
        print("No public keys were imported, did you use a proper key and include the headers?")
    else:
        print("Key was imported successfully. Please certify the key in Kleopatra for security purposes. ")

# lists the key details, for debugging at the moment.
def print_key_details(myGnu):

    # List all keys
    keys = myGnu.list_keys()

    # Print details of each key
    for key in keys:
        print(f"Key ID: {key['keyid']}")
        print(f"Fingerprint: {key['fingerprint']}")
        print(f"Length: {key['length']}")
        print(f"Algorithm: {key['algo']}")
        print(f"Creation Date: {key['date']}")
        print(f"User IDs: {', '.join(key['uids'])}")
        print(f"Expires: {key.get('expires', 'Never')}")
        print(f"Trust: {key.get('trust', 'Unknown')}")
        print("-" * 40)

