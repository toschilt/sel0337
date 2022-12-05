from smbus import SMBus

from time import sleep
addr = 0x8
bus = SMBus(1)

while(True):
	val = bus.read_i2c_block_data(addr, 0, 2)
	pos1 = val[0] * 2 ** 8
	pos2 = val[1]
	pos = pos1 + pos2
	print(pos)
	sleep(0.150)
