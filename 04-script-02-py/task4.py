#!/usr/bin/env python3
import sys
import socket


def f_prev_values(file):
    values_arr = []
    try:
        file_import = open(f'{file}')
    except FileNotFoundError:
        return values_arr
    url_ip_list = file_import.read().splitlines()
    file_import.close()
    for host in url_ip_list:
        values_arr.append(host.split(' - '))
    return values_arr


def f_match_ip(result_new, result_old):
    for host_new, host_old in zip(result_new, result_old):
        if host_new[0] == host_old[0] and host_new[1] != host_old[1]:
            print(f'[ERROR] {host_new[0]} IP mismatch: {host_old[1]} {host_new[1]}')
    return


cur_values_arr = []
cur_values_list = []
param = sys.argv
prev_values_file = 'service_check_result.txt'
url_services = ['drive.google.com', 'mail.google.com', 'google.com']

prev_values_arr = f_prev_values(prev_values_file)

check_result_file = open(f'{prev_values_file}', 'w')
for i, url in enumerate(url_services):
    ip_addr = socket.gethostbyname(url)
    cur_values_list.insert(i, f'{url} - {ip_addr}')
    cur_values_arr.append(cur_values_list[i].split(' - '))
    print(cur_values_list[i])
    check_result_file.write(f'{cur_values_list[i]}\n')
check_result_file.close()

if len(param) > 1 and param[1] == '-m':
    f_match_ip(cur_values_arr, prev_values_arr)
