import os
import pyaes

## Open the encrypted file

file_name = "test.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Decryptation key

key = b"testinransomware"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remove encrypted file

os.remove(file_name)

## Create a new decrypted file

new_file = "test.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypt_data)
new_file.close()
