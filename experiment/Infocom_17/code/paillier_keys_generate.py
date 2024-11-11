from phe import paillier
import pickle

# 生成公私钥
public_key, private_key = paillier.generate_paillier_keypair()

public_key = pickle.dumps(public_key)
private_key = pickle.dumps(private_key)
# 将公私钥的值保存到txt文件中
with open('public_key_B.txt', 'wb') as file:
    file.write(public_key)
with open('private_key_B.txt', 'wb') as file:
    file.write(private_key)

