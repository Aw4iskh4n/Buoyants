from Crypto.Cipher import AES
import base64

# Sample image URL
image_url = "https://yt3.googleusercontent.com/ytc/AIf8zZS6XDo-M7dlTyolU_yBAp-cmqn0EfZ8AGkKa9yItg=s900-c-k-c0x00ffffff-no-rj"

# AES key (must be 16, 24, or 32 bytes long)
key = bytes.fromhex("165a547310ddf1dd83b6826f7313344c")

# Pad the data to be encrypted
pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
image_url_padded = pad(image_url)

# Encrypt the data
cipher = AES.new(key, AES.MODE_ECB)
encrypted_bytes = cipher.encrypt(image_url_padded.encode())

# Encode the encrypted data in Base64
encrypted_base64 = base64.b64encode(encrypted_bytes)

# Make the Base64 string URL-safe
encrypted_base64_url_safe = encrypted_base64.decode().replace('+', '-').replace('/', '_').rstrip('=')

encrypted_base64_url_safe
