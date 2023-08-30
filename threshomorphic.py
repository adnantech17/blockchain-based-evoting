from phe import paillier
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Util.number import bytes_to_long, long_to_bytes

def genKeys(n_length = 1024):
    public_key, private_key = paillier.generate_paillier_keypair(n_length=256)
    return (public_key) , (private_key)

def decode(byte_string):
    return bytes_to_long(byte_string)
def encode(value):
    return long_to_bytes(value)

def splitKey(k , n, key):

    shares = Shamir.split(k , n , key)
    return shares

def combineKey(shares):
    key = decode(Shamir.combine(shares))
    return key


p , s = genKeys(256)
print(s.p , s.q)

share = splitKey(2 ,5 , s.q)


key = combineKey([share[0], share[2]])
print(key)