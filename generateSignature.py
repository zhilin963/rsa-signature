from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512
from Crypto.Hash import SHA
import base64

def rsa_sign(plaintextPath, skPath):
    #get secret key
    with open(skPath) as f:
        secretKey = f.read()
    secretKeyBytes = base64.b64decode(secretKey)
    sk = RSA.importKey(secretKeyBytes)
    sender = PKCS1_v1_5.new(sk)
    #get plaintext
    with open(plaintextPath) as f1:
        plaintext = f1.read()
    hash_value = SHA.new(plaintext.encode('utf-8'))
    signature = base64.b64encode(sender.sign(hash_value))
    #generate signature file
    with open('Signature.txt', 'wb') as f2:
        f2.write(signature)
    return signature


def main():
    textPath = 'updateFile.py'
    secretKeyPath = 'secretKey.txt'


    signature = rsa_sign(textPath, secretKeyPath)
    signaturePath = 'Signature.txt'
    print('Signature was created successfully!')


if __name__ ==  "__main__":
    main()
