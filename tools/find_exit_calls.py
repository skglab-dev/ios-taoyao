import struct

with open('sysimage/rootfs/usr/sbin/bluetoothd', 'rb') as f:
    data = f.read()

targets = [0x10065fc50, 0x100660184]
for target in targets:
    print(f'Searching calls to {hex(target)}:')
    for pc in range(0x100000000, 0x100000000 + len(data) - 4, 4):
        off = pc - 0x100000000
        insn = struct.unpack('<I', data[off:off+4])[0]
        # BL opcode: bits 26-31 == 0b100101 (0x25)
        if (insn >> 26) == 0x25:
            imm26 = insn & 0x3FFFFFF
            if imm26 & (1 << 25):
                imm26 -= (1 << 26)
            dest = pc + (imm26 << 2)
            if dest == target:
                print(f'  call at {hex(pc)}')
                # disassemble surrounding instructions
                print('    next instructions:')
                for n in range(4, 16, 4):
                    next_insn = struct.unpack('<I', data[off+n:off+n+4])[0]
                    print(f'      +{n}: {hex(next_insn)}')

