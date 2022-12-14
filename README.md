# RSA Signature and Verification  
Python programming example

## 1.Description  
A Python program to implement RSA signature and verification, in order to prove whether the message was sent by a specific sender.  

## 2.Operation 

* **Signature Generation**
: Licensee generates a digital signature with his own private key.  

* **File Compression**
: Licensee packages and compresses the signature and files.  

* **File Upload/Retrieval**
: Licensee uploads the compressed package to a file system, e.g. IPFS. Device retrieves the package by a hash value, then downloads the package to local storage. (exact procedure and the transfer of hash value is not described here)
 <div align=center><img width="650" height="400" src="https://github.com/zhilin963/rsa-signature/blob/main/IMG/ipfs.jpg" />  </div>  

* **File Decompression**
: Device decompresses the package.  

* **Signature Verification**
: Device verifies the signature with Licensee's public key.


## 3.Instructions
* generate the digital signature using Licensee's secret key.  
`python generateSignature.py`

* compress the update file and signature into a zip package.  
`python compressFile.py`  

* decompress the package.    
`python decompressFile.py`  

* verify the digital signature with Licensee's public key.    
`python verifySignature.py`
