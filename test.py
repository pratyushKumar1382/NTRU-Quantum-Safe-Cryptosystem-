from ntru import NTRUKey, generate_key
from poly import Polynomial as poly
from rsa_list import generate_keys, encrypt, decrypt 
from utils import *
import time

def deserialize(ply):
    lst = []
    for coeff in ply._coeff:
        lst.append(coeff)
    return lst



def main():

    key = generate_key()

    # message = [1,1,0,0,-1,-1,-1,1,1,0,1,-1,1,0,-1,-1,1,0,0,1,0,1,-1,1]
    message = [12, 3, 4]

    message1 = "Hello World"
    print("Plain text Message: ", message1,"\n")
    print("NTRU:\n")

    start_time = time.perf_counter()
    m = string_to_encoded_array(message1)
    m = poly(m, len(m))
    c = key.encrypt(m, key._h)
    end_time = time.perf_counter()
    print("Time taken in NTRU encryption: ", end_time - start_time, " s")

    print("Encrypted Message: ", c,"\n")

    
    start_time = time.perf_counter()
    d = key.decrypt(c)
    d = deserialize(d)
    d = encoded_array_to_string(d)
    end_time = time.perf_counter()
    print("Time taken in NTRU decryption: ", end_time - start_time, " s")


    print("Decrypted Message: ", d,"\n")

    print("RSA:\n")
    rsa_pub, rsa_pvt = generate_keys() 

    start_time = time.perf_counter()
    c = encrypt(message, rsa_pub)
    end_time = time.perf_counter()
    print("Time taken in RSA encryption: ", end_time - start_time, " s")
    print("Encrypted Message: ", c, "\n")

    start_time = time.perf_counter()
    d = decrypt(c, rsa_pvt)
    end_time = time.perf_counter()
    print("Time taken in RSA decryption: ", end_time - start_time, " s")
    print("Decrypted message: ", d, "\n")


        
if __name__ == '__main__':
    print("Testing NTRU Key Object Operations")
    main()