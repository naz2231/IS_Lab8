import ecdsa
import math
from time import perf_counter_ns


def hack(bit_num: int):
    product = math.pow(2, bit_num - 1)

    if product < math.pow(2, bit_num):
        product += 1
        for i in range(2, int(product)):
            if (product % i) == 0:
                print([x for x in range(1, int(product))])
            else:
                break
    else:
        pass


privateKey = ecdsa.SigningKey.generate()
publicKey = privateKey.verifying_key

with open("privateKey.pem", "wb") as file:
    file.write(privateKey.to_pem())

with open("publicKey.pem", "wb") as file:
    file.write(publicKey.to_pem())

with open("privateKey.pem") as file:
    privateKey = ecdsa.SigningKey.from_pem(file.read())

message = "Anyone who has never made a mistake has never tried anything new. - Albert EinsteinAnyone who has never made a mistake has never tried anything new. - Albert EinsteinAnyone who has never made a mistake has never tried anything new. - Albert EinsteinAnyone who has never made a mistake has never tried anything new. - Albert EinsteinAnyone who has never made a mistake has never tried anything new. - Albert Einstein"
messageBytes = bytes(
    message, encoding="utf-8")

startTime = perf_counter_ns()
sig = privateKey.sign(messageBytes)
print(
    f'\nSigning time: {(perf_counter_ns() - startTime)/1000000} miliseconds\n')

with open("signature", "wb") as file:
    file.write(sig)

publicKey = ecdsa.VerifyingKey.from_pem(open("publicKey.pem").read())

with open("signature", "rb") as f:
    sig = f.read()

try:
    startTime = perf_counter_ns()
    publicKey.verify(sig, messageBytes)
    print(
        f'\nVerification time: {(perf_counter_ns() - startTime)/1000000} miliseconds\n')
    print(sig)
    print(privateKey)
    print(publicKey)
    print("verificated")
except ecdsa.BadSignatureError:
    print("wrong signature")
