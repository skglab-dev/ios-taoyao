import struct

with open("/home/kristoforusapm/hakios-taoyao/sysimage/rootfs/usr/sbin/bluetoothd", "rb") as f:
    data = f.read()

targets = [0x100881810, 0x100883b75, 0x100882373, 0x10088431f]

for t in targets:
    b = struct.pack("<Q", t)
    pos = 0
    while True:
        pos = data.find(b, pos)
        if pos == -1:
            break
        print(f"Pointer to 0x{t:x} found at offset 0x{pos:x} (va 0x{0x100000000 + pos:x})")
        pos += 8
