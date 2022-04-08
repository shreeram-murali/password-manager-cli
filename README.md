# password-manager-cli
A command-line based local password manager for all your passwords.

---

## What's this?

This is a command-line based local password manager that you can trust. You'll be able to store encrypted passwords using Fernet (asymmetric) encryption wherein your passwords is encrypted using key that only you have access to. 

Should you really use this for your passwords? Probably not. There aren't recovery options if you lose your key. 

## Installation

Clone the repository your preferrred directory -- this is the location where your encrypted passwords will be stored.

```
git clone https://github.com/shreeram-murali/password-manager-cli.git
```

## Usage

Open up the terminal and `cd` into this directory. 

Type `python3 keychain.py -h` for help for directions on how to use the command-line arguments. There are three things you can do with this application:

1. Generate a new key with which you'll be able to encrypt your password
2. Encrypt and store your password
3. Access an already-stored password with your key 

### Generate

Type in:

```
$ python3 keychain.py --generate True
```
You'll see:

```
Keep the following key in a secured location
JSP_k6FfwaKKIOD140tnYLg94uZ8uSjKRcYqIC7tXnI=
```

This key is like your master password, especially if you're using the same key to encrypt all your passwords. Store it in a secure location. 

### Store

Type in:

```
python3 keychain.py --store True
```

You'll see:

```
Please enter your key (as a string):JSP_k6FfwaKKIOD140tnYLg94uZ8uSjKRcYqIC7tXnI=Enter the ID or username you want to store: aol
Enter your password: 
Password: 
Confirm password, enter it again: 
Password: 
Password sucessfully encrypted and written to vault
```

### Access

Type in:

```
python3 keychain.py --access True
```

You'll see:

```
Please enter your key (as a string): JSP_k6FfwaKKIOD140tnYLg94uZ8uSjKRcYqIC7tXnI=
Enter the ID or username you want to access: aol
Your password is: 
 	rubyonrails 
```

---

## Fernet encryption

Fernet encryption is an implementation of symmetric authenticated cryptography. More on the function in the [documentation](https://cryptography.io/en/latest/fernet/). 

## Future

- Containerize the application
- Add an option to specify a path to a text file on the command line that contains the key
- Pull requests are welcome

