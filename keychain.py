import argparse
from cryptography.fernet import Fernet

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate', type=bool, default=False, required=False, help='True to generate a key')
    parser.add_argument('--access', type=bool, default=False, required=False, help='True to access existing passwords')
    args = parser.parse_args()

    if args.generate == True:
        key = Fernet.generate_key()
        print("Keep the following key in a secured location.")
        print(key)
        print("Use python3 keychain.py --generate True to generate a key")
    
    if args.access == True:
        """Code to get passwords"""