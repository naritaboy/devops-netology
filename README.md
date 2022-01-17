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
