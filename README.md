# RSA Signature and Verification  
Python programming example

## 1.Description  
A Python program to implement RSA signature and verification, in order to prove whether the message was sent by a specific sender.  

## 2.Operation
![image](https://github.com/zhilin963/rsa-signature/blob/main/IMG/ipfs.jpg)  

* **Signature Generation**
: Licensee generates a digital signature with his own private key.  

* **File Compression**
: Licensee packages and compresses the signature and files.  

* **File Upload/Retrieval**
: Licensee uploads the compressed package to a file system, e.g. IPFS. Device retrieves the package by a hash value, then downloads the package to local storage. (exact procedure and the transfer of hash value is not described here)    

* **File Decompression**
: Device decompresses the package.  

* **Signature Verification**
: Device verifies the signature with Licensee's public key.
