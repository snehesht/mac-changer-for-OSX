#! /usr/bin/python
from subprocess import Popen,PIPE
import random,time


source = ['1','2','3','4','5','6','7','8','9','0']


#process = Popen(['ifconfig','en0', 'down'], stdout=PIPE,stderr=PIPE)
#stdout,stderr = process.communicate()



def genMac():
	tmp = []
	for i in range(6):
		for j in range(2):
			tmp.append(random.choice(source))
		if len(tmp) != 17:
			tmp.append(':')
	mac = ''.join(i for i in tmp)
	return mac


def main():
	currMac = Popen(['sudo','ifconfig','en0','ether'], stdout=PIPE,stderr=PIPE)
	stdout,stderr = currMac.communicate()
	currMac = stdout
	randmac = genMac()
	changeMac = Popen(['sudo','ifconfig','en0','ether',randmac], stdout=PIPE,stderr=PIPE)
	stdout,stderr = changeMac.communicate()
	if stderr != '':
		print('an error occured.')
		print(stderr)
		exit()
	time.sleep(3)
	StopWifi = Popen(['sudo','ifconfig','en0', 'down'], stdout=PIPE,stderr=PIPE)
	stdout,stderr = StopWifi.communicate()
	time.sleep(4)
	StartWifi = Popen(['sudo','ifconfig','en0','up'], stdout=PIPE,stderr=PIPE)
	stdout,stderr = StartWifi.communicate()

	print('MAC address changed succesfully'+'\n')
	print('Old MAC\n{0}'.format(currMac))
	print('New MAC\n{0}'.format(randmac))
if __name__=="__main__":
	main()