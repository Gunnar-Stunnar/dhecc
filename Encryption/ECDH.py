import Utils
import Config

print("******* Public Key Generation *********")
PublicKey = Utils.EccMultiply(Config.GPoint, Config.privKey)
print("the private key:")
print(Config.privKey)
print("the uncompressed public key (not address):")
print(PublicKey)
print("the uncompressed public key (HEX):")
print("04" + "%064x" % PublicKey[0] + "%064x" % PublicKey[1])
print("the official Public Key - compressed:")
if PublicKey[1] % 2 == 1:  # If the Y value for the Public Key is odd.
   print("03"+str(hex(PublicKey[0])[2:-1]).zfill(64))
else:  # Or else, if the Y value is even.
   print("02"+str(hex(PublicKey[0])[2:-1]).zfill(64))

# 1. Establish relations between Eliptic function and diffie Hellam
# 2. Alice has (Da,Qa) BOB has (Db,Qb) D is public key while Q is privte key
# 3. (xk,yk) = Da*Qb  (xk,yk) = Db * Qa
# 4. Secret is xk which will be used another idea is use XOR with xk and yk
# 5. plug it into AES or fern