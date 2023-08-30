from phe import paillier
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Util.number import bytes_to_long, long_to_bytes

class Threshomorphic:
    def __init__(self):
        self.publicKey, self.privateKey = None, None
    def genKeys(self, n_length=1024):
        self.publicKey, self.privateKey = paillier.generate_paillier_keypair(n_length=n_length)
    def encode(self, value):
        return long_to_bytes(value)

    def decode(self, byte_string):
        return bytes_to_long(byte_string)

    def splitKey(self, k, n, key):
        shares = Shamir.split(k, n, key)
        shares = [(idx, self.decode(splittedKey)) for (idx, splittedKey) in shares]
        return shares

    def combineKey(self, datas):

        pShares = []
        qShares = []

        for data in datas:
            data = data.split('.')
            if len(data) == 3:
                pShares.append((int(data[0]), self.encode(int(data[1]))))
                qShares.append((int(data[0]), self.encode(int(data[2]))))
            else:
                raise ValueError("Invalid key")

        pKey = self.decode(Shamir.combine(pShares))
        qKey = self.decode(Shamir.combine(qShares))

        privateKey = paillier.PaillierPrivateKey(self.publicKey, pKey, qKey)
        return privateKey

    def savePublicKey(self):
        with open('public-keys/pub.key', "wb") as f:
            f.write(self.encode(self.publicKey.n))

    def savePrivateKey(self, k, n):
        pShares = self.splitKey(k, n, self.privateKey.p)
        qShares = self.splitKey(k, n, self.privateKey.q)

        for pShare, qShare in zip(pShares, qShares):
            with open(f'private-keys/{pShare[0]}.key', "w") as f:
                f.write(f'{pShare[0]}.{pShare[1]}.{qShare[1]}')

    def encryptVote(self, vote):
        return [self.publicKey.encrypt(x) for x in vote]

    def decryptVote(self, encryptedVote):
        return [self.publicKey.decrypt(x) for x in encryptedVote]

    def loadPublicKey(self):
        with open('public-keys/pub.key', "rb") as f:
            key = f.read()
        return paillier.PaillierPublicKey(self.decode(key))
    def loadAndSavePublicKey(self):
        with open('public-keys/pub.key', "rb") as f:
            key = f.read()
        self.publicKey = paillier.PaillierPublicKey(self.decode(key))
        return self.publicKey

    def getPublicKey(self):
        return self.publicKey

    def getPrivateKey(self):
        return self.privateKey

# Example usage
if __name__ == "__main__":
    keyManager = Threshomorphic()
    keyManager.genKeys(256)
    # print(keyManager.getPrivateKey().p, keyManager.getPrivateKey().q)
    keyManager.savePrivateKey(2, 3)
    keyManager.savePublicKey()
    print(keyManager.getPublicKey().n)
    print(keyManager.loadPublicKey().n)
    # key1 = input('Input First key:')
    # key2 = input('Input Second key:')
    # privateKey = keyManager.combineKey([key1, key2])
    # secretNumber = 5
    # encrypted = keyManager.getPublicKey().encrypt(secretNumber)
    # print(privateKey.decrypt(encrypted))
