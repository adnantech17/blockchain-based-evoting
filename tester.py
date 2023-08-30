from votingSystem import VotingSystem
from phe import paillier

tm = VotingSystem()

tm.genKeys()

val = [12345, 0]

enc = tm.encryptVote(val)
print(enc)
enc2 = tm.encryptVote([-100, 0])
print(enc2)
enc[0] = paillier.EncryptedNumber(tm.getPublicKey(
), enc[0]) + paillier.EncryptedNumber(tm.getPublicKey(), enc2[0])
enc[1] = paillier.EncryptedNumber(tm.getPublicKey(
), enc[1]) + paillier.EncryptedNumber(tm.getPublicKey(), enc2[1])
print(enc)
print(tm.decryptVote(enc))

# public_key = tm.loadAndSavePublicKey()

# key1 = input('Input First key:')
# key2 = input('Input Second key:')
# privateKey = tm.combineKey([key1, key2])
# secretNumber = 5
# encrypted = tm.getPublicKey().encrypt(secretNumber)
# print(privateKey.decrypt(encrypted))
