from pwn import *


level1b = process("../release/level1b")

print("[*] recived {}".format(level1b.recvline().strip()))
level1b.sendline(b"\x01" * 14)
print("[*] recived {}".format(level1b.recvline()))
