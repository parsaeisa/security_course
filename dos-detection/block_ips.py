from ipaddress import ip_address
from os import execv


def get_malware_ips():
    try:
        file1 = open('/home/snapp/Documents/Uni /CS/project/ddos-detection/malware_ips.txt', 'r')
        Lines = file1.readlines()
        malware_ips = set()
        
        for line in Lines:
            for ip_address in line.strip().split(','):
                malware_ips.add(ip_address)

        return malware_ips
    except:
        return []
