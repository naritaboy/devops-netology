#!/usr/bin/env python3

import socket


def f_last_check_data(file):
    url_list = []
    ip_list = []
    try:
        file_import = open(f'{file}')
    except FileNotFoundError:
        return url_list, ip_list
    last_check = file_import.read().splitlines()
    file_import.close()
    for host in last_check:
        url_list.append(host.split(' - ')[0])
        ip_list.append(host.split(' - ')[1])
    return url_list, ip_list


def f_check_main(file, url_serv):
    url_last_check, ip_last_check = f_last_check_data(file_last_check)
    file_check = open(f'{file}', 'w')
    for url_check in url_serv:
        ip_check = socket.gethostbyname(url_check)
        result_check = f'{url_check} - {ip_check}'
        print(result_check)
        file_check.write(f'{result_check}\n')
        for i in range(len(url_last_check)):
            if url_last_check[i] == url_check and ip_last_check[i] != ip_check:
                print(f'[ERROR] {url_check} IP mismatch: {ip_last_check[i]} {ip_check}')
    file_check.close()
    return


url_services = ['drive.google.com', 'mail.google.com', 'google.com']
file_last_check = 'IP.txt'

f_check_main(file_last_check, url_services)
