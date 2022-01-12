#Домашнее задание к занятию «2.4. Инструменты Git»

1. git show aefea
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Update CHANGELOG.md
2. git show 85024d3
tag: v0.12.23
3. git show b8d720 или git show b8d720^ и git show b8d720^2
У коммита b8d720 2 родителя:
commit 56cd7859e05c36c06b56d013b55a252d0bb7e158
commit 9ea88f22fc6269854151c571162c5bcf958bee2b
4. git log v0.12.23..v0.12.24 --pretty=format:'%h %s'
b14b74c49 [Website] vmc provider links
3f235065b Update CHANGELOG.md
6ae64e247 registry: Fix panic when server is unreachable
5c619ca1b website: Remove links to the getting started guide's old location
06275647e Update CHANGELOG.md
d5f9411f5 command: Fix bug when using terraform login on Windows
4b6d06cc5 Update CHANGELOG.md
dd01a3507 Update CHANGELOG.md
225466bc3 Cleanup after v0.12.23 release
5. git log -S 'func providerSource(' --oneline
8c928e835
6. Сначала найдем в каком файле определена функция globalPluginDirs
git grep 'func globalPluginDirs('
plugins.go
Далее найдем коммиты, где была изменена функция в этом файле
git log -L :globalPluginDirs:plugins.go --oneline
78b122055
52dbf9483
41ab0aef7
66ebff90c
8364383c3
7. git log -S 'func synchronizedWriters(' --pretty=format:'%h %an <%ae>' | tail -1
5ac311e2a Martin Atkins <mart@degeneration.co.uk>
