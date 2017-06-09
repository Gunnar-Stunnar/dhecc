
# --- HOW THIS WORKS ---
# 1. FIRST BOTH PARTY'S CREATE RANDOM KEYS OF SAME SIZE BETWEEN 160 - 512 BITS THEN TURN IT TO HEX --> PLUG INTO OBJECT WHEN CREATING IT A = AESCipher(KEY)
# 2. NEXT BOTH PARTY'S SEND THERE PUBLIC KEYS (AKA us getPubKey()) TO EACH OTHER
# 3. LAST BOTH PARTY'S USE THE FUNCTION DHEC AND PLUG THE OTHERS PARTY'S SHARED PUBLIC KEY INTO IT TO GENERATE THE KEY
# 4. NOW YOU ARE READY TO ENCRYPT


# --- NOTES ---
# DO NOT USE WHILE INTOXICATED
# I LEFT EVERYONE USING THIS TO GENERATE THEIR OWN KEY, DO NOT FUCK THIS UP
# BEST TO DO IF CHATTING, IS GENERATE A KEY EVERY TIME YOU START A SESSION
# HAVE FUN!!!

import base64
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import UTILECC


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s)-1:])]


class AESCipher:

    #put in any size key of hex exe : 0x... this should be 160 bit for medium term secutiry for 512 for long term security said my the UN
    def __init__(self, key):
        self.privKey = key
        self.Pubkey = UTILECC.genPubKey(key) # generating off of the Configs generator point

    # after getting other Public key from other party then put it into this function
    def DHEC(self, otherPubKey):
        self.key = hashlib.sha256(UTILECC.DHEC(self.privKey, otherPubKey)).digest()

    def getPubKey(self):
            return self.Pubkey

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))











