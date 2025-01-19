import hmac
import datetime as dt

masterkey = 9876543210
serial = 1234567890
nonce = 12345

print("Id,Chip serial,Timestamp,Admin Key")
for i in range(1,6):
    chipserial = hex(serial).encode('utf-8')
    session_nonce = hex(nonce).encode('utf-8')
    key = bytes(chipserial+session_nonce)
    adminkey = hmac.new(key, digestmod='sha512')
    adminkey.update(hex(masterkey).encode('utf-8'))
    print(f"{i},{serial},{nonce},{adminkey.hexdigest()}")
    serial = serial + 1
    nonce = nonce + 1

