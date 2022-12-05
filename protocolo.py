from smbus import SMBus


addr = 0x8 # bus address
bus = SMBus(1) # /dev/ic2-1
flag = True
print ("Digite 1 para ON ou 0 para OFF")

while flag:
	ledstate = input(">>>> ")
	if ledstate == "1":
		bus.write_byte(addr, 0x1)
	elif ledstate == "0":
		bus.write_byte(addr, 0x0)
	else:
		flag = False
