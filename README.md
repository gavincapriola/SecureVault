---

# SecureVault: A Simple Python Password Manager

SecureVault is a lightweight, easy-to-use password manager built with Python. It helps users generate strong passwords and securely store them using advanced encryption. This project aims to provide a basic yet powerful tool for managing passwords without the need for complex setups or external dependencies.

## Features

- **Password Generation**: Automatically generates strong, secure passwords.
- **Encryption**: Uses Fernet encryption to securely store passwords.
- **Simple Storage**: Stores all passwords in an encrypted file, minimizing the risk of exposure.
- **Easy Retrieval**: Quickly retrieve your passwords with a simple command.
- **CLI Interface**: A user-friendly command-line interface for easy navigation and usage.

## Usage

To use SecureVault, navigate to the project directory and run the `main.py` script:

```
python main.py
```

Follow the on-screen prompts to generate new passwords, retrieve existing ones, or exit the program:

1. **Generate and save a new password**: Select this option to create a new password for a service. SecureVault will generate a strong password, encrypt it, and save it securely.

2. **Retrieve a password**: If you need to look up a password for a specific service, choose this option and enter the service name.

3. **Exit**: Safely exits the password manager.
