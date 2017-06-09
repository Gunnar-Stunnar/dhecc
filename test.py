import Encryption
import os

random_key1 = os.urandom(32)
random_key2 = os.urandom(32)
random_key1f = int(("".join("{:02x}".format(ord(c)) for c in random_key1)), 16)
random_key2f = int(("".join("{:02x}".format(ord(c)) for c in random_key2)), 16)


print(" -=keys=- ")
print(random_key1f)
print(random_key2f)

part1 = Encryption.AESCipher(random_key1f)
part2 = Encryption.AESCipher(random_key2f)

print("\n-=public keys=-")
print(part1.getPubKey())
print(part2.getPubKey())

part1.DHEC(part2.getPubKey())
part2.DHEC(part1.getPubKey())


print("\n-=TEST ROUNDS=-")
ent1 = part1.encrypt("howdy" + " " + 128*",")
print(part2.decrypt(ent1))

ent2 = part2.encrypt("howdy2")
print(part1.decrypt(ent2))
