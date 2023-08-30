from voting import Threshomorphic 

tm = Threshomorphic()


public_key = tm.loadAndSavePublicKey()

key1 = input('Input First key:')
key2 = input('Input Second key:')
privateKey = tm.combineKey([key1, key2])
secretNumber = 5
encrypted = tm.getPublicKey().encrypt(secretNumber)
print(privateKey.decrypt(encrypted))

