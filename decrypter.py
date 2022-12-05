import os 
import pyaes

file = open("test.txt", "rb")
file_data = file.read()
file.close()

key = b"Key with you want"
aes = pyaes.AESModeOfOperationCTR(key)

data_decrypt = aes.decrypt(file_data)

os.remove(file_name)

new_file = open("test.txt", "wb")
new_file.write(data_decrypt)
new_file.close()

