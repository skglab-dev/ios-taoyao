import struct
with open("/home/kristoforusapm/hakios-taoyao/sysimage/rootfs/usr/sbin/bluetoothd", "rb") as f:
    data = f.read()

brks = []
for i in range(0, len(data) - 4, 4):
    w = struct.unpack("<I", data[i:i+4])[0]
    if (w & 0xffe0001f) == 0xd4200000:
        imm = (w >> 5) & 0xffff
        brks.append((i, imm))

print(f"Total brk instructions found: {len(brks)}")
for off, imm in brks:
    print(f"offset 0x{off:x} (va 0x{0x100000000 + off:x}): brk #{imm}")
