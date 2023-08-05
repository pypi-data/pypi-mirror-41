from .utils.base import Base64
from .utils.binary import BinaryToAscii
from .utils.der import encodeSequence, encodeInteger, removeSequence, removeInteger


class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s

    def toDer(self):
        return encodeSequence(encodeInteger(self.r), encodeInteger(self.s))

    def toBase64(self):
        return Base64.encode(self.toDer())

    @classmethod
    def fromDer(cls, string):
        rs, empty = removeSequence(string)
        if empty != "":
            raise Exception("trailing junk after DER sig: %s" % BinaryToAscii.hexFromBinary(empty))
        r, rest = removeInteger(rs)
        s, empty = removeInteger(rest)
        if empty != "":
            raise Exception("trailing junk after DER numbers: %s" % BinaryToAscii.hexFromBinary(empty))
        return Signature(r, s)

    @classmethod
    def fromBase64(cls, string):
        der = Base64.decode(string)
        return cls.fromDer(der)
