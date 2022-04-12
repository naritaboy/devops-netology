#!/usr/bin/env python
import socket

url_services = ['drive.google.com', 'mail.google.com', 'google.com']
url_last_check = list(range(len(url_services)))
ip_last_check = list(range(len(url_services)))

try:
    file_import = open('IP.txt')
    last_check = file_import.read().splitlines()
    file_import.close()

    for i in range(len(last_check)):
        host = last_check[i].split(' - ')
        url_last_check[i] = host[0]
        ip_last_check[i] = host[1]

except FileNotFoundError:
    print('First start script. An IP.txt file has been created in the current directory.')

file_check = open('IP.txt', 'w')

for service in url_services:
    ip_check = socket.gethostbyname(service)
    result_check = f'{service} - {ip_check}'
    print(result_check)
    file_check.write(f'{result_check}\n')

    for j in range(len(url_last_check)):
        if url_last_check[j] == service and ip_last_check[j] != ip_check:
            print(f'[ERROR] {service} IP mismatch: {ip_last_check[j]} {ip_check}')

file_check.close()
