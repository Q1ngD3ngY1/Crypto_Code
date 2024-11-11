from phe import paillier
import pickle
with open('private_key_B.txt', 'rb') as file:
    pri = file.read()
private_key = pickle.loads(pri)
with open('public_key_B.txt', 'rb') as file:
    pub = file.read()
public_key = pickle.loads(pub)
#public_key = paillier.PaillierPublicKey(int())
print(public_key)
print(private_key)
c = public_key.encrypt(123123)
print(private_key.decrypt(c))