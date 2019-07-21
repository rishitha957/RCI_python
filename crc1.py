def crc16(data: bytes, poly=0x11021):
    
    #data = bytearray(data)
    crc = 0xFFFF
    for b1 in data:
        b = '0x'+b1
        b = int(b,16)
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    
    return crc & 0xFFFF

data = 'C3 04 03 1B 9F 73 3B 96 27 7A 94 0A D5 61 90 5A 6A 42 70'
data = data.split(" ")

# for i in range(len(data)):
#     data[i] = '0x'+data[i]

print(crc16(data))