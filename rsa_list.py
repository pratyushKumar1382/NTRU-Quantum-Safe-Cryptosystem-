import rsa


def generate_keys():
    (pub_key, priv_key) = rsa.newkeys(512)
    return pub_key, priv_key


def encrypt(int_list, pub_key):
    encrypted_list = []
    for num in int_list:
        encrypted_list.append(rsa.encrypt(num.to_bytes(1, 'big', signed=True), pub_key))
    return encrypted_list


def decrypt(encrypted_list, priv_key):
    decrypted_list = []
    for enc in encrypted_list:
        decrypted_list.append(int.from_bytes(rsa.decrypt(enc, priv_key), 'big', signed=True))
    return decrypted_list


if __name__ == "__main__":

    original_list = [-1, 0, 1]
    
    
    public_key, private_key = generate_keys()
    
    encrypted = encrypt_list(original_list, public_key)
    print("Encrypted List:", encrypted)
    
    decrypted = decrypt_list(encrypted, private_key)
    print("Decrypted List:", decrypted)
