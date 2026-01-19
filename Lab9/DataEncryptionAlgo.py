from Crypto.Cipher import DES
import binascii

def pad(text):
  while len(text) % 8 != 0:
    text += ' '
  return text

def des_encrypt(key, plaintext):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return binascii.hexlify(encrypted_text).decode('utf-8')

def des_decrypt(key, ciphertext):
    des = DES.new(key, DES.MODE_ECB)
    encrypted_text = binascii.unhexlify(ciphertext)
    decrypted_text = des.decrypt(encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()  # Remove padding spaces

key = b'8bytekey'
plaintext = "HELLODES"


print("Plaintext:", plaintext )
cipher = des_encrypt(key, plaintext)
print("Encrypted (Hex):", cipher )
decrypted = des_decrypt(key, cipher)
print("Decrypted:", decrypted)