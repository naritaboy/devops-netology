#!/usr/bin/env python
import socket

url_services = ['drive.google.com', 'mail.google.com', 'google.com']
url_last_check = []
ip_last_check = []

try:
    file_import = open('IP.txt')
    last_check = file_import.read().splitlines()
    file_import.close()

    for host in last_check:
        url_last_check.append(host.split(' - ')[0])
        ip_last_check.append(host.split(' - ')[1])

except FileNotFoundError:
    print('First start script. An IP.txt file has been created in the current directory.')

file_check = open('IP.txt', 'w')

for url_check in url_services:
    ip_check = socket.gethostbyname(url_check)
    result_check = f'{url_check} - {ip_check}'
    print(result_check)
    file_check.write(f'{result_check}\n')

    for i in range(len(url_last_check)):
        if url_last_check[i] == url_check and ip_last_check[i] != ip_check:
            print(f'[ERROR] {url_check} IP mismatch: {ip_last_check[i]} {ip_check}')

file_check.close()

