import argparse
from cryptography.fernet import Fernet
import pandas as pd

from manager import Passwords

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', type=bool, default=False, required=False, help='True to generate a key')
    parser.add_argument('--access', type=bool, default=False, required=False, help='True to access existing passwords')
    parser.add_argument('--store', type=bool, default=False, required=False, help='Store a new password')
    parser.add_argument('--keypath', type=str, default=None, required=False, help='Path to text file containing your key')
    args = parser.parse_args()

    if args.generate == True:
        key = Fernet.generate_key()
        print("Keep the following key in a secured location")
        print(key)
    
    if args.access == True:
        input_key = input('Please enter your key (as a string): ')
        # Implement better methods of entering the key
        username = input('Enter the ID or username you want to access/store: ')

    
    print("Tips:\nUse python3 keychain.py --generate True to generate a key")
    print("Use python3 keychain.py --access True to access your saved passwords\n")