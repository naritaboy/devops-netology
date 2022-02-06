# Домашнее задание
## Домашнее задание к занятию "3.4. Операционные системы, лекция 2"
### Вопрос 1
Создал unit-файл для node_exporter, учел возможность добавления опций к запускаемому процессу через внешний файл и поместил unit в автозагрузку

`sudo systemctl cat node_exporter`
```
# /etc/systemd/system/node_exporter.service
[Unit]
Description=Prometheus exporter for hardware and OS metrics exposed by *NIX kernels
Documentation=https://prometheus.io/docs/guides/node-exporter/
After=network.target

[Service]
ExecStart=/opt/node_exporter/bin/node_exporter $EXT_OPTS
EnvironmentFile=-/etc/opt/node_exporter/options
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
`cat /etc/opt/node_exporter/options`
```
EXT_OPTS="--collector.tcpstat"
``` 

`sudo systemctl status node_exporter`
```
● node_exporter.service - Prometheus exporter for hardware and OS metrics exposed by *NIX kernels
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-02-06 08:30:16 PST; 1min 50s ago
       Docs: https://prometheus.io/docs/guides/node-exporter/
   Main PID: 713 (node_exporter)
      Tasks: 3 (limit: 1055)
     Memory: 13.6M
     CGroup: /system.slice/node_exporter.service
             └─713 /opt/node_exporter/bin/node_exporter --collector.tcpstat
```
### Вопрос 2
По умолчанию включены все необходимые метрики для мониторинга процессора, памяти, диска и сети.  
Можно включить сборщик tcpstat (—collector.tcpstat)

`curl -s http://localhost:9100/metrics | grep tcp`
```
node_scrape_collector_duration_seconds{collector="tcpstat"} 0.000354582
node_scrape_collector_success{collector="tcpstat"} 1
# HELP node_tcp_connection_states Number of connection states.
# TYPE node_tcp_connection_states gauge
node_tcp_connection_states{state="established"} 3
node_tcp_connection_states{state="listen"} 6
node_tcp_connection_states{state="rx_queued_bytes"} 0
node_tcp_connection_states{state="tx_queued_bytes"} 0
```

### Вопрос 3
Установил netdata и ознакомился с метриками
![netdata-screenshot](./media/3_4-os/netdata1.png)

### Вопрос 4
В выводе dmesg есть сообщение об обнаружении виртуализации

`dmesg -T | grep virtual`
```
[Sat Feb  5 07:21:35 2022] systemd[1]: Detected virtualization parallels.
```

### Вопрос 5
Максимальное количество файловых дескрипторов, которые может открыть процесс

`sysctl -a | grep fs.nr_open`
```
fs.nr_open = 1048576
```

Другой лимит – **ulimit -n** (the maximum number of open file descriptors)

`ulimit -a | grep open`
```
open files                      (-n) 1024
```

### Вопрос 6
`ps a`
```
    PID TTY      STAT   TIME COMMAND
      1 pts/0    S+     0:00 sleep 1h
      2 pts/1    S      0:00 -bash
     24 pts/1    R+     0:00 ps a
```

### Вопрос 7
Это форк-бомба

`dmesg -T | tail -1`
```
[Sat Feb  5 11:45:36 2022] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-22.scope
```

cgroup - механизм ядра Linux, который изолирует и ограничивает использование ресурсов группе процессов.

https://www.kernel.org/doc/Documentation/cgroup-v1/pids.txt  
Process Number Controller  
The process number controller is used to allow a cgroup hierarchy to stop any new tasks from being fork()'d or clone()'d after a certain limit is reached.  
Since it is trivial to hit the task limit without hitting any kmemcg limits in place, PIDs are a fundamental resource. As such, PID exhaustion must be preventable in the scope of a cgroup hierarchy by allowing resource limiting of the number of tasks in a cgroup.

`ulimit -a | grep process`
```
max user processes              (-u) 3421
```
`ulimit -u `

---

## Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

1. chdir()
2. /usr/share/misc/magic.mgc  
Дополнительно использовал `man file` и `man magic`  
3. Посмотреть файловый дескриптор файла с логом  
`lsof -p <PID> | grep file.log`  
Очистить содержимое командой:  
`cat /dev/null >/proc/<PID>/fd/3`  
Место на диске освобождается, проверено командой `df -h`. Хотя поле SIZE в `lsof -p <PID> -s | grep file.log` не обнуляется.  
4. Зомби-процессы не занимают ресурсы, но блокируют записи в таблице процессов, размер которой ограничен для каждого пользователя и системы в целом.
5. `sudo opensnoop-bpfcc -d 1`  
/proc/interrupts  
/proc/stat  
/proc/irq/20/smp_affinity  
/proc/irq/0/smp_affinity  
/proc/irq/1/smp_affinity  
/proc/irq/8/smp_affinity  
/proc/irq/12/smp_affinity  
/proc/irq/14/smp_affinity  
/proc/irq/15/smp_affinity   
6. uname()  
Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.
7. При использовании `;` команды выполняются последовательно в порядке очереди, возвращается статус последней выполненной команды.  
При использовании `&&` следующая команда выполняется в случае успешного завершения предыдущей команды (статус 0). Возвращается статус последней выполненной команды в списке.  
`set -e` — немедленный выход из оболочки, если команда завершилась с ошибкой.  
Выход из оболочки не выполняется, если (но не только при этом) команда завершилась с ненулевым кодом, которая является частью любой команды, выполняемой в списке через &&, за исключением команды, следующей за конечным символом &&  
Поэтому при определенных условиях имеет смысл использовать `&&` с примененным `set -e`  
8. `set -euxo pipefail`  
**-e** разобран в предыдущем ответе  
**-u** Считать неустановленные переменные и параметры, отличные от специальных параметров "@" и "*", ошибкой при расширении параметров. При попытке раскрытия неустановленной переменной или параметра оболочка печатает сообщение об ошибке и, если не интерактивна, завершает работу с ненулевым статусом.  
**-x** После расширения каждой простой команды, для команды, команды case, команды выбора или арифметики для команды, отобразите расширенное значение PS4, за которым следует команда и ее расширенные аргументы или связанный список слов.  
**-o pipefail** Если установлено, возвращаемое значение конвейера — это значение последней (самой правой) команды для выхода с ненулевым статусом или ноль, если все команды в конвейере завершаются успешно. Эта опция отключена по умолчанию.
9. `ps axo stat --sort=stat | grep -v STAT | cut -c-1 | uniq -c | sort -r`  
     69 S  
     46 I  
      1 R  
Наиболее часто встречается статус S - interruptible sleep (waiting for an event to complete)

##Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"
1. `type cd`  
cd is a shell builtin  
Команда cd выполняется в самой оболочке, не порождает новый процесс.  
Команда выбирает рабочую директорию оболочки, поэтому логично, что команда выполняется внутри этой оболочки.
2. `grep -c <some_string> <some_file>`
3. systemd
4. `ls /empty 2>/dev/pts/X`
5. `cat <file1 >file2`
6. `echo "pew pew" >/dev/tty1`
7. Командой `bash 5>&1` создан новый файловый дескриптор с выводом на stdout, т.е. на терминал данной сессии /proc/$$/fd5 -> /dev/pts/X  
echo `netology > /proc/$$/fd/5` выведет сообщение в терминал текущей сессии
8. `cat file 2>&1 >&5 | wc -w`  
Перенаправляем stderr в stdout, а stdout в fd5 -> /dev/pts/X
9. Файл /proc/$$/environ содержит начальные переменные окружения  
Аналогичный вывод можно получить командой `env`
10. /proc/\<PID\>/cmdline  
Файл содержит полную командную строку запуска процесса, кроме зомби-процесса  
/proc/\<PID\>/exe  
В Linux 2.2 и более поздних версиях этот файл представляет собой символическую ссылку, содержащую фактический путь к выполняемой команде.  
В Linux 2.0 и более ранних версиях - является указателем на исполняемый двоичный файл и отображается как символическая ссылка.
11. `grep sse /proc/cpuinfo`  
Мой процессор не поддерживает набор инструкций SSE
12. При выполнении команды по ssh не открывается новый терминал, поэтому не выделяется pty  
Можно добавить ключ -t  
`ssh -t localhost 'tty'`  
vagrant@localhost's password:  
/dev/pts/1
13. reptyr \<PID\>
14. tee - читает из стандартного ввода и записывает в стандартный вывод и файлы  
Перенаправлением занимается процесс shell'а, который запущен без sudo под вашим пользователем, а tee записывает в файл и его можно вызвать с sudo


##Домашнее задание к занятию "3.1. Работа в терминале, лекция 1"

1. Установил **Parallels**
2. Установил Vagrant + плагин Parallels  
`vagrant plugin list`  
vagrant-parallels (2.2.4, global)
3. \+
4. Использовал `config.vm.box = "bento/ubuntu-20.04-arm64"`
5. Процессор: 2 CPU  
Память: 1024 MB  
Дисковое пространство: 64 GB
6. Для добавления оперативной памяти или процессора ВМ необходимо добавить в Vagrantfile строчки и перезагрузить ВМ:  
`config.vm.provider "virtualbox" do |v|`  
`  v.memory = [ram_size]`  
`  v.cpus = [cpu]`  
`end`
7. \+
8. Длина журнала **history** описывается переменными:  
line 937 HISTFILESIZE - максимальное количество строк  
line 955 HISTSIZE - количество команд  
ignoreboth - значение опции HISTCONTROL, включает в себя:  
ignorespace - не сохранять в истории команды, начинающиеся с пробела  
ignoredups - не сохранять строку, если она совпадает с предыдущей  
9. Символы **{}** используются в составных командах, когда необходимо выполнить команды в текущей оболочке.  
line 287
10. `touch file{1..100000}`  
Предварительно увеличить размер стека  
`ulimit -s 65536`  
`touch file{1..300000}`  
`ls -l file* | wc`  
 300000 2700000 16388895
11. `[[ -d /tmp ]]`  
Возвращает истину, если существует директория /tmp  
**[[ ]]** - проверяется условие внутри и возвращается 0 или 1  
**-d** — истина, если файл существует и это директория
12. `type -a bash`  
bash is /usr/bin/bash  
bash is /bin/bash  
`echo $PATH`  
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin  
`mkdir /tmp/new_path_directory`  
`cp /usr/bin/bash /tmp/new_path_directory`  
`PATH=/tmp/new_path_directory/:$PATH`  
`type -a bash`  
bash is /tmp/new_path_directory/bash  
bash is /usr/bin/bash  
bash is /bin/bash
13. **at** выполняет команды в указанное время.  
**batch** выполняет команды, когда load average падает ниже 1,5 или значения, указанного при вызове atd (`atd [-l load_avg]`).
14. \+




##Домашнее задание к занятию «2.4. Инструменты Git»
1. `git show aefea`\
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545\
Update CHANGELOG.md
2. `git show 85024d3`\
tag: v0.12.23
3. `git show b8d720` или `git show b8d720^` и `git show b8d720^2`\
У коммита b8d720 2 родителя:\
commit 56cd7859e05c36c06b56d013b55a252d0bb7e158\
commit 9ea88f22fc6269854151c571162c5bcf958bee2b
4. `git log v0.12.23..v0.12.24 --pretty=format:'%h %s'`\
b14b74c49 [Website] vmc provider links\
3f235065b Update CHANGELOG.md\
6ae64e247 registry: Fix panic when server is unreachable\
5c619ca1b website: Remove links to the getting started guide's old location\
06275647e Update CHANGELOG.md\
d5f9411f5 command: Fix bug when using terraform login on Windows\
4b6d06cc5 Update CHANGELOG.md\
dd01a3507 Update CHANGELOG.md\
225466bc3 Cleanup after v0.12.23 release
5. `git log -S 'func providerSource(' --oneline`\
8c928e835
6. Сначала найдем в каком файле определена функция globalPluginDirs\
`git grep 'func globalPluginDirs('`\
plugins.go\
Далее найдем коммиты, где была изменена функция в этом файле\
`git log -L :globalPluginDirs:plugins.go --oneline`\
78b122055\
52dbf9483\
41ab0aef7\
66ebff90c\
8364383c3
7. `git log -S 'func synchronizedWriters(' --pretty=format:'%h %an <%ae>' | tail -1`\
5ac311e2a Martin Atkins <mart@degeneration.co.uk>
