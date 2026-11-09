import struct

with open("/home/kristoforusapm/hakios-taoyao/sysimage/rootfs/usr/sbin/bluetoothd", "rb") as f:
    data = f.read()

target_pages = {0x100881000, 0x100882000, 0x100883000, 0x100884000}

matches = []
for off in range(0, min(len(data), 0x700000) - 8, 4):
    pc = 0x100000000 + off
    w = struct.unpack("<I", data[off:off+4])[0]
    if (w & 0x9f000000) == 0x90000000:
        immlo = (w >> 29) & 3
        immhi = (w >> 5) & 0x7ffff
        imm = (immhi << 2) | immlo
        if imm & (1 << 20):
            imm -= (1 << 21)
        target_page = (pc & ~0xfff) + (imm << 12)
        if target_page in target_pages:
            matches.append((pc, off, target_page))

print(f"Found {len(matches)} ADRP candidates targeting these pages:")
for pc, off, tp in matches:
    print(f"0x{pc:x} (offset 0x{off:x}) -> page 0x{tp:x}")
