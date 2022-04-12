#!/usr/bin/env python3

import os

bash_command = ["cd ~/Netology/sysadm-homeworks", "pwd", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
result_os_line = result_os.split('\n')

for result in result_os_line:
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f'{result_os_line[0]}/{prepare_result}')
