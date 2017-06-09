# DHECC
Diffie Hellman Elliptic Curve Key exchange automated Encrypting system using AES. This was a fun side project to get to play with encryption and practice Python.

## How To Use

First add the Imports.
```
import Encryption
import os # optional if you want to generate your own keys.
```

Next both partys create a Random key that is 32 bytes long.
```
random_key1 = os.urandom(32) # os random provides a more securely generated value.
random_key1f = int(("".join("{:02x}".format(ord(c)) for c in random_key1)), 16)

# party 2
random_key2 = os.urandom(32)
random_key2f = int(("".join("{:02x}".format(ord(c)) for c in random_key1)), 16)

```
After this the both partys making use of this will instantiate the AESCipher class in Encryption and pass the randomly generated key to it.
```
# party 1 
party1 = Encryption.AESCipher(random_key1f)

# party 2
party2 = Encryption.AESCipher(random_key2f)

```
Once this is done both partys will then obtain their public keys and send them to each other.

```
# party 1 
party1_pubKey = party1.getPubKey()

# party 2 
party2_pubKey = party2.getPubKey()
```

```
# party 1 
party1.DHEC(party2.getPubKey())

## party 2
party2.DHEC(party1.getPubKey())
```

After this then both partys are able to start encrypting

```
ent1 = part1.encrypt("howdy" + " " + 128*",")
print(part2.decrypt(ent1))

ent2 = part2.encrypt("howdy2")
print(part1.decrypt(ent2))
```
## Disclaimer 

I am not fully done with this and will not be held responsible if their are any found vulnerability in it that are exsploited on your application. PLEASE, send me a message if you see any vulnerability

THANK YOU
