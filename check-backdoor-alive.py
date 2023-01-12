'''
jammer.py


**TO-DO before run**

1. Re-new ip_list
'''

from pwn import *
from andctf import *

debug = True

def main():
    global debug 
    debug = input("[*] Debug: [y/n]") != 'n'

    a = int(input("""
    [*] Menu
    1. Scan all team & chal
    2. Jam specific team & chal
    """))

    if a==1:
        scan()
    else:
        ip = input("[*] ip: ")
        port = int(input("[*] port: "))
        jamming(ip,port)


if __name__ == "__main__":
    main()
