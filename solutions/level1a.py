from pwn import *


level1a = process("../release/level1a")

print("[*] recived {}".format(level1a.recvline().strip()))
level1a.sendline(b"\x01" * 14)
print("[*] recived {}".format(level1a.recvline()))