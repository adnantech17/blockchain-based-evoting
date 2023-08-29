from phe import paillier
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Util.number import bytes_to_long, long_to_bytes

public_key, private_key = paillier.generate_paillier_keypair(n_length=256)
secret_number_list = [1, 2, 3]
secret_number_list2 = [3.141592653, 300, 2]

print("before thres", private_key.q)

shares = Shamir.split(2, 5, private_key.q)
# print([bytes_to_long(share[1]) for share in shares])

for idx, share in shares:
    print("Index #%d: %s" % (idx, bytes_to_long(share)))

# new_shares = []
# for x in range(2):
#     in_str = input("Enter index and share separated by comma: ")
#     idx, share = [s.strip() for s in in_str.split(",")]
#     new_shares.append((int(idx), long_to_bytes(int(share))))

key = Shamir.combine(shares)

print("after thresh", bytes_to_long(key))

newPrivateKey = paillier.PaillierPrivateKey(
    public_key, private_key.p, private_key.q)


print(str(private_key))

encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]
encrypted_number_list2 = [public_key.encrypt(x) for x in secret_number_list2]
result = [x + y for x, y in zip(encrypted_number_list, encrypted_number_list2)]

print([newPrivateKey.decrypt(x) for x in result])
