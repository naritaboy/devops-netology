#!/usr/bin/env python3

import os
import sys

rep_path = "~/Netology/sysadm-homeworks"
param_path = sys.argv

if len(param_path) > 1:
    rep_path = param_path[1]

bash_command = [f"cd {rep_path}", "pwd", "git status 2>&1"]
result_os = os.popen(' && '.join(bash_command)).read()
result_os_line = result_os.split('\n')

for result_error in result_os_line:
    if result_error.find('not a git repository') != -1:
        print(f'Directory {rep_path} is not a local git repository')
        sys.exit()

for result in result_os_line:
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f'{result_os_line[0]}/{prepare_result}')
