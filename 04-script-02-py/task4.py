#!/usr/bin/env python3

import socket


def f_last_check_data(file):
    url_ip_arr = []
    try:
        file_import = open(f'{file}')
    except FileNotFoundError:
        return url_ip_arr
    url_ip_list = file_import.read().splitlines()
    file_import.close()
    for i, host in enumerate(url_ip_list):
        url_ip_arr.append(host.split(' - '))
    return url_ip_arr


url_services = ['drive.google.com', 'mail.google.com', 'google.com']
file_last_check = 'IP.txt'

url_last_arr = f_last_check_data(file_last_check)
file_check = open(f'{file_last_check}', 'w')

for url_check in url_services:
    ip_check = socket.gethostbyname(url_check)
    result_check = f'{url_check} - {ip_check}'
    print(result_check)
    for host in url_last_arr:
        if host[0] == url_check and host[1] != ip_check:
            print(f'[ERROR] {url_check} IP mismatch: {host[1]} {ip_check}')

    file_check.write(f'{result_check}\n')
file_check.close()

