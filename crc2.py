import crcmod.predefined
crc16_func = crcmod.predefined.mkCrcFun('crc-16')
hex(crc32_func('C3 04 03 1B 9F 73 3B 96 27 7A 94 0A D5 61 90 5A 6A 42 70'))