from pwn import *
try:
	f = process('./guessing-game.py')
	sleep(0.25)
	out = str(f.read())
	print(out)
	out1 = out.strip('b')
	number = int(out1[-5:-3])
	x=0

	while x <= number:
		sleep(0.10)
		f.send(str(x)+'\n')
		x+=1
		sleep(0.10)
		output = f.read()
		if 'Congratlations' in str(output):
			print(output)
except:
	pass