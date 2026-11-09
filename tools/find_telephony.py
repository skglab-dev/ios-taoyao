with open("/home/kristoforusapm/hakios-taoyao/sysimage/rootfs/usr/sbin/bluetoothd", "rb") as f:
    data = f.read()

targets = [
    b"com.apple.commcenter.coretelephony.xpc",
    b"com.apple.commcenter",
    b"com.apple.telephonyutilities",
    b"callcapabilities",
    b"callstatecontroller",
]

for t in targets:
    pos = 0
    while True:
        pos = data.find(t, pos)
        if pos == -1:
            break
        print(f"Found '{t.decode('latin1')}' at offset 0x{pos:x} (va 0x{0x100000000 + pos:x})")
        pos += len(t)
