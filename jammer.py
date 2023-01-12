'''
jammer.py


**TO-DO before run**

1. Re-new ip_list
'''

from pwn import *
from andctf import *
import os 
import random
import time

debug = False


def rand()->int:
    return random.randrange(jamming_length)

def jamming_pattern()->bytearray:
    pattern = bytearray(os.urandom(random.randint((jamming_length*4//5), jamming_length)))

    if random.random() > 0.8:
        return pattern

    # Jamming with blacklist
    for jam in jamming_blacklist:
        idx = rand()
        pattern[idx:idx+len(jam)] = jam

    # Jamming with random IP
    idx = rand()    
    for i in range(3):
        tmp = (str(random.randrange(0x100))+".").encode()
        pattern[idx:idx+len(tmp)] = tmp
        idx += len(tmp) 

    tmp = str(random.randrange(0x100)).encode()
    pattern[idx:idx+len(tmp)] = tmp 
    
    return pattern

def jamming(ip: str, port: int,timeout:float):
    global debug
    
    print("[*] Initializing Jammer")
    idx = 0
    try:
        p = remote(ip, port)

    except:
        print("[*] Jamming Failed - Open Error: " + ip_to_team(ip) + " - " + port_to_chal(port))
        print()
        return

    start = time.time()

    while True:
        p.sendline(jamming_pattern())
        
        try:
            p.sendline(jamming_pattern())
        except:
            print("[*] Jamming Failed - Send Error: " + ip_to_team(ip) + " - " + port_to_chal(port))
            print()
            return
        
        if idx % 0x200 == 0 and debug:
            print("[*] Jamming * "+str(idx)+"...")
            print(jamming_pattern())
        
        sleep(1/jamming_speed)

        if time.time()-start > timeout:
            return

        


def main():
    global debug 
    print("Jammer - Saturate specific team's chal")
    debug = input("[*] Debug: [y/n] ") != 'n'


    ip = input("[*] ip: ")[:-1]
    port = int(input("[*] port: "))
    jamming(ip,port,5)


if __name__ == "__main__":
    main()
