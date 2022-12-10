import hashlib


def encrypt_password(password):
    # Create a hash object
    hash_obj = hashlib.sha256()

    # Use the update method to add the password to the hash object
    hash_obj.update(password.encode('utf-8'))

    # Get the encrypted password as a hexadecimal string
    encrypted_password = hash_obj.hexdigest()

    return encrypted_password


# Example usage
pw = "apakaka"
encrypted_pw = encrypt_password(pw)
print(encrypted_pw)  # Prints the encrypted password
