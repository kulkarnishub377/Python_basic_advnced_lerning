import argparse
import json
import os
import sys
from cryptography.fernet import Fernet, InvalidToken

DATA_FILE = "passwords.json"
KEY_FILE = "secret.key"


def generate_key():
    """Generates a new Fernet key and saves it to a file."""
    if os.path.exists(KEY_FILE):
        print(f"Error: Key file '{KEY_FILE}' already exists. Refusing to overwrite.")
        print("Delete it manually if you really want to generate a new key.")
        sys.exit(1)

    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved to {KEY_FILE}. Keep it safe!")


def load_key():
    """Loads the Fernet key from the file."""
    if not os.path.exists(KEY_FILE):
        print(f"Error: Key file '{KEY_FILE}' not found.", file=sys.stderr)
        print("Run 'python manager.py generate-key' first.", file=sys.stderr)
        sys.exit(1)
    
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def load_passwords():
    """Loads the encrypted passwords dictionary from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    
    with open(DATA_FILE, "r") as data_file:
        try:
            return json.load(data_file)
        except json.JSONDecodeError:
            return {}


def save_passwords(data):
    """Saves the encrypted passwords dictionary to the JSON file."""
    with open(DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4)


def add_password(service, username, password):
    """Encrypts and stores a new password for a service."""
    key = load_key()
    f = Fernet(key)

    data = load_passwords()

    # Create payload and encrypt it
    payload = f"{username}||{password}"
    encrypted_payload = f.encrypt(payload.encode()).decode()

    data[service.lower()] = encrypted_payload
    save_passwords(data)

    print(f"Successfully added credentials for {service}.")


def get_password(service):
    """Retrieves and decrypts a password for a service."""
    key = load_key()
    f = Fernet(key)

    data = load_passwords()
    lookup = service.lower()

    if lookup not in data:
        print(f"Error: No credentials found for service '{service}'.", file=sys.stderr)
        sys.exit(1)

    encrypted_payload = data[lookup].encode()

    try:
        decrypted_payload = f.decrypt(encrypted_payload).decode()
        username, password = decrypted_payload.split("||", 1)
        
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {password}")
    
    except InvalidToken:
        print("Error: Invalid or corrupted decryption key. Cannot read passwords.", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Secure CLI Password Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: generate-key
    subparsers.add_parser("generate-key", help="Generate a new encryption key (run once)")

    # Command: add
    parser_add = subparsers.add_parser("add", help="Add a new password")
    parser_add.add_argument("--service", required=True, help="Name of the service/website")
    parser_add.add_argument("--username", required=True, help="Username or email")
    parser_add.add_argument("--password", required=True, help="The password")

    # Command: get
    parser_get = subparsers.add_parser("get", help="Retrieve an existing password")
    parser_get.add_argument("--service", required=True, help="Name of the service/website")

    args = parser.parse_args()

    if args.command == "generate-key":
        generate_key()
    elif args.command == "add":
        add_password(args.service, args.username, args.password)
    elif args.command == "get":
        get_password(args.service)


if __name__ == "__main__":
    main()
