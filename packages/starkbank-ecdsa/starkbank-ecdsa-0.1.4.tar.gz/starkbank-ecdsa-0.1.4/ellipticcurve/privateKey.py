from random import SystemRandom
from .math import multiply
from .curve import curvesByOid, supportedCurves
from .utils.binary import BinaryToAscii
from .utils.der import fromPem, removeSequence, removeInteger, removeObject, removeOctetString, removeConstructed, toPem, encodeSequence, encodeInteger, encodeBitstring, encodeOid, encodeOctetString, encodeConstructed
from .publicKey import PublicKey
from .curve import secp256k1


class PrivateKey:

    def __init__(self, curve=secp256k1, secret=None):
        self.curve = curve
        self.secret = secret or SystemRandom().randrange(1, curve.N)

    def publicKey(self):
        curve = self.curve
        publicPoint = multiply(curve.G, n=self.secret, A=curve.A, P=curve.P, N=curve.N)
        return PublicKey(x=publicPoint.x, y=publicPoint.y, curve=curve)

    def toString(self):
        return BinaryToAscii.stringFrom(number=self.secret, length=self.curve.length())

    def toDer(self):
        encodedPublicKey = self.publicKey().toString(encoded=True)
        return encodeSequence(
            encodeInteger(1),
            encodeOctetString(self.toString()),
            encodeConstructed(0, encodeOid(*self.curve.oid)),
            encodeConstructed(1, encodeBitstring(encodedPublicKey)),
        )

    def toPem(self):
        return toPem(der=self.toDer(), name="EC PRIVATE KEY")

    @classmethod
    def fromPem(cls, string):
        privkeyPem = string[string.index("-----BEGIN EC PRIVATE KEY-----"):]
        return cls.fromDer(fromPem(privkeyPem))

    @classmethod
    def fromDer(cls, string):
        s, empty = removeSequence(string)
        if empty != "":
            raise Exception("trailing junk after DER privkey: %s" % BinaryToAscii.hexFromBinary(empty))

        one, s = removeInteger(s)
        if one != 1:
            raise Exception("expected '1' at start of DER privkey, got %d" % one)

        privkeyStr, s = removeOctetString(s)
        tag, curveOidStr, s = removeConstructed(s)
        if tag != 0:
            raise Exception("expected tag 0 in DER privkey, got %d" % tag)

        oidCurve, empty = removeObject(curveOidStr)
        if empty != "":
            raise Exception("trailing junk after DER privkey curve_oid: %s" % BinaryToAscii.hexFromBinary(empty))

        curve = curvesByOid.get(oidCurve)
        if not curve:
            raise Exception("Unknown curve with oid %s. I only know about these: %s" % (
                oidCurve, ", ".join([curve.name for curve in supportedCurves]))
            )

        if len(privkeyStr) < curve.length():
            privkeyStr = "\x00" * (curve.lenght() - len(privkeyStr)) + privkeyStr

        return cls.fromString(privkeyStr, curve)

    @classmethod
    def fromString(cls, string, curve=secp256k1):
        return PrivateKey(secret=BinaryToAscii.numberFrom(string), curve=curve)
