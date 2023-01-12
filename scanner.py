'''
scanner.py


**TO-DO before run**

1. Re-new ip_list
'''

from pwn import *
from andctf import *
import os 
import random

debug = True

def print_result(success_map: dict, fail_list: list):
    os.system("clear")

    print("========== Sleeping Chals ==========")
    for key in sorted(success_map.keys(), key = lambda x: x[0]):
        print(ip_to_team(key[0]) + " - " + port_to_chal(key[1]))


    print("========== Alive Chals ==========")
    for key in sorted(fail_list, key = lambda x: x[0]):
        print(ip_to_team(key[0]) + " - " + port_to_chal(key[1]))


def scan():
    socket_map = {}
    fail_list = []
    
    print("[*] Initializing Scanner")

    for ip in ip_list:
        for port in port_list:
            fail_list.append((ip,port))

    while True:
        change = False
        for ip in ip_list:
            for port in port_list:

                if (ip,port) in fail_list:            
                    try:
                        p = remote(ip, port)
                        socket_map[(ip,port)] = p
                        fail_list.remove((ip, port))
                        change = True
                    except:
                        continue

                if (ip,port) in socket_map:
                    try:
                        socket_map[(ip,port)].send(os.urandom(random.randint(100, 1000)))
                    except:
                        del socket_map[(ip,port)]
                        fail_list.append((ip, port))
                        change = True

        sleep(0.7582)
        if change:
            print_result(socket_map,fail_list)  

def main():
    global debug 
    debug = input("[*] Debug: [y/n]") != 'n'
    scan()
    

if __name__ == "__main__":
    main()
