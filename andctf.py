ip_list =  ['192.168.200.135']
# ip_list =  ['10.0.3.'+str(i) for i in range(14)]

team_list = ['team_'+str(i) for i in range(14)]

port_list = [i for i in range(30000,30010)]
chal_list = ['test_'+str(i) for i in range(10)]



jamming_length = 2000
jamming_blacklist = [b'nc', b'>&', b'/bin/sh', b'flag', b'dev', b'tcp']

def ip_to_team(ip: str)->str:
    return team_list[ip_list.index(ip)]

def team_to_ip(team: str)->str:
    return ip_list[team_list.index(team)]
    

def port_to_chal(port: int)->str:
    return chal_list[port_list.index(port)]