from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512
from Crypto.Hash import SHA
import base64

def rsa_verify(signaturePath, plaintextPath, pkPath):
    #get public key
    with open(pkPath) as f:
        publicKey = f.read()
    publicKeyBytes = base64.b64decode(publicKey)
    pk = RSA.importKey(publicKeyBytes)
    receiver = PKCS1_v1_5.new(pk)
    #get plaintext
    with open(plaintextPath) as f1:
        plaintext = f1.read()
    hash_value = SHA.new(plaintext.encode('utf-8'))
    #get signature
    with open(signaturePath) as f2:
        signature = f2.read()
    #verify signature
    return receiver.verify(hash_value, base64.b64decode(signature))

def main():
    textPath = 'UpdateFile.py'
    publickKeyPath = 'publicKey.txt'
    signaturePath = 'Signature.txt'

    result = rsa_verify(signaturePath, textPath, publickKeyPath)
    if result == True:
        print('Signature verification was successful!')
    elif result == False:
        print('Signature verification failed!')

if __name__ ==  "__main__":
    main()
