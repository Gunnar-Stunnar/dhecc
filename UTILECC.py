#!/usr/bin/python
import Config
import base64

def modinv(a, n=Config.Pcurve):  # Extended Euclidean Algorithm/'division' in elliptic curves its the idenity
    lm, hm = 1, 0
    low, high = a % n, n  # Define
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n


def ECadd(a, b):  # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0], Config.Pcurve)) % Config.Pcurve
    xr = (LamAdd*LamAdd-a[0]-b[0]) % Config.Pcurve
    yr = (LamAdd*(a[0]-xr)-a[1]) % Config.Pcurve
    return xr, yr


def ECdouble(a):  # This is called point doubling, also invented for EC.
    Lam = ((3*a[0]*a[0]+Config.Acurve) * modinv((2*a[1]), Config.Pcurve)) % Config.Pcurve
    x = (Lam*Lam-2*a[0]) % Config.Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Config.Pcurve
    return x, y


def EccMultiply(GenPoint, ScalarHex):  # Double & add. Not true multiplication
    if ScalarHex == 0 or ScalarHex >= Config.N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint
    for i in range(1, len(ScalarBin)):  # This is invented EC multiplication.
        Q = ECdouble(Q)  # print "DUB", Q[0]; print
        if ScalarBin[i] == "1":
            Q = ECadd(Q, GenPoint)  # print "ADD", Q[0]; print
    # print(Q)
    return Q


def compressKey(pubKey):
    x = hex(pubKey[0])
    y = hex(pubKey[1])
    str = x + "," + y;
    #print(type(base64.b64encode(str)))
    return base64.b64encode(str)


def decompressKey(comKey):

    decode = base64.b64decode(comKey)
    x = decode.split(',')[0]
    y = decode.split(',')[1]
    return int(x[2:-1], 16), int(y[2:-1], 16)


def genPubKey(key):
    return compressKey(EccMultiply(Config.GPoint, key))

def DHEC(privkey, pubkey):
        return compressKey(EccMultiply(decompressKey(pubkey), privkey))


if __name__=="__main__":
    privKey1 = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E;
    pirvKeys2 = 0xA0DC65CFCA79D873CBEA0AC274015B9526505DBACED385155425F7337704983E;

    print("******* Public Key Generation *********")
    PublicKey1 = EccMultiply(Config.GPoint, privKey1)
    PublicKey2 = EccMultiply(Config.GPoint, pirvKeys2)
    print("the private key:")
    print(PublicKey1)
    print(PublicKey2)
    print(compressKey(PublicKey1))
    print(compressKey(PublicKey2))
    print(decompressKey(compressKey(PublicKey1)))
    print(decompressKey(compressKey(PublicKey2)))

    key1 = EccMultiply(PublicKey1, pirvKeys2)
    key2 = EccMultiply(PublicKey2, privKey1)

    print("****** Output of Keys *******")

    print (compressKey(key1))
    print (compressKey(key2))


    print("\n\n\n-----******* Public Key Generation *********----")
    PublicKey = EccMultiply(Config.GPoint, Config.privKey)
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
