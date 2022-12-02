from numpy import true_divide
import pandas as pd
from block_ips import get_malware_ips


def dos_detect(requests_threshold=15):
    requests_df = pd.read_csv('/home/snapp/Documents/Uni /CS/project/ddos-detection/request_logger.csv')
    all_ips = list(requests_df['IP'].unique())
    malware_ips = []
    for ip in all_ips:
        ip_df = requests_df[requests_df['IP'] == ip]
        if ip_df.shape[0] >= requests_threshold:
            malware_ips.append(ip)

    file_object = open('/home/snapp/Documents/Uni /CS/project/ddos-detection/malware_ips.txt', 'a')

    something_added = False
    for malware_ip in malware_ips:
        malware_ips_till_now = get_malware_ips()
        
        # guard detections 
        if malware_ip in malware_ips_till_now :
            continue
        if malware_ip == '':
            continue

        something_added = True
        file_object.write(malware_ip)
        file_object.write(',')

    if something_added:
        file_object.write('\n')

    file_object.close()
    return malware_ips


if __name__ == '__main__':
    print('detection started ...')
    dos_detect()
