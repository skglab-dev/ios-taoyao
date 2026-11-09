import struct

with open("/home/kristoforusapm/hakios-taoyao/sysimage/rootfs/usr/sbin/bluetoothd", "rb") as f:
    data = f.read()

# Let's find abort stub in __stubs:
# In previous steps:
# __stubs is at 0x10065e390 to 0x100661420
# Let's search symbol table or stubs for abort
# Let's check where 'abort' is in strings / symbols
pos = 0
aborts = []
while True:
    pos = data.find(b"abort\x00", pos)
    if pos == -1:
        break
    aborts.append(pos)
    pos += 6

print(f"Found 'abort\\0' at: {[hex(p) for p in aborts]}")
