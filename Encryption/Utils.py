#!/usr/bin/python
import Config


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
            print(Q)
    return Q



