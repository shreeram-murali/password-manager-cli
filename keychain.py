import argparse
from cryptography.fernet import Fernet
import pandas as pd
import getpass

import manager

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', type=bool, default=False, required=False, help='True to generate a key')
    parser.add_argument('--access', type=bool, default=False, required=False, help='True to access existing passwords')
    parser.add_argument('--store', type=bool, default=False, required=False, help='Store a new password')
    args = parser.parse_args()

    vault = 'vault/secrets.csv'
    tips = True

    if args.generate == True:
        key = Fernet.generate_key()
        print("\nKeep the following key in a secured location")
        print(key.decode())
        tips = False
    
    if args.access == True:
        input_key = input('\nPlease enter your key (as a string): ')
        username = input('Enter the ID or username you want to access: ')
        passwords_df = pd.read_csv(vault)
        for i, val in enumerate(passwords_df['username']):
            if val == username.lower():
                token = passwords_df['token'][i]
                pwd = manager.decrypt(token, input_key)
                print("Your password is: \n \t{} \n ".format(pwd.decode()))
        tips = False
    
    if args.store == True:
        input_key = input('\nPlease enter your key (as a string): ')
        username = input('Enter the ID or username you want to store: ')
        while True:
            print("Enter your password: ")
            pwd1 = getpass.getpass()
            print("Confirm password, enter it again: ")
            pwd2 = getpass.getpass()
            if pwd1 == pwd2:
                break
            else:
                print("The two passwords did not match, please try again.\n")
        token = manager.encrypt(pwd1, input_key)
        passwords_df = pd.read_csv(vault)
        appendicitis = pd.DataFrame({'username': [username], 'token': [token.decode()]})
        passwords_df = passwords_df.append(appendicitis, ignore_index=True)
        passwords_df.to_csv(vault)
        print("Password sucessfully encrypted and written to vault")
        tips = False

    if tips:
        print("\nTips:\n \t1. Type python3 keychain.py -h for help.")
        print("\t2. Use the same key for all your passwords or store your individual keys securely.")
        print("\t3. This was made as a personal project. Please use a real password manager.")