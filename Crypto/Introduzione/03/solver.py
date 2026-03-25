from base64 import *
b64="ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
b10=664813035583918006462745898431981286737635929725
print(b64decode(b64).decode())
print((b10).to_bytes(20,'big').decode())