# Домашнее задание к занятию "4.1. Командная оболочка Bash: Практические навыки"

## Обязательная задача 1

| Переменная | Значение | Обоснование                                                                                                                                             |
|------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `c`        | a+b      | Переменной `c` присваиватеся значение без привязки к переменным `a` и `b`                                                                               |
| `d`        | 1+2      | Переменной `d` присваивается значение с учетом значений переменных `a` и `b` без арифметических вычислений, т.к. переменная `d` неявно определена       |
| `e`        | 3        | Переменной `e` присваивается значение результата арифметичеких вычислений со значениями переменных `a` и `b`, т.к. выражение заключено в двойные скобки |

## Обязательная задача 2

```
#!/bin/bash
url_serv="https://localhost:4757"
#while ((1==1))
while true
do
	curl -s $url_serv >/dev/null 2>&1
	exit_code=$?
	if [ $exit_code -ne 0 ]
	then
		date >> curl.log
	else
		break
	fi
done
```

## Обязательная задача 3

```
#!/bin/bash
hosts=("192.168.0.1" "173.194.222.113" "87.250.250.242")
port=80
steps=5
logfile=./log
for (( i=1; i<=$steps; i++ ))
	do
	echo "$(date) Step $i" >>$logfile
	for host in ${hosts[@]}
		do
		nc -zw1 $host $port >/dev/null 2>&1
		exit_code=$?
		if [ $exit_code -eq 0 ]
		then 
			echo "Host $host is available on port $port" >>$logfile
		else
			echo "Host $host is not available on port $port" >>$logfile
		fi
	done
done
```

## Обязательная задача 4

```
#!/bin/bash
hosts=("192.168.0.1" "173.194.222.113" "87.250.250.242")
port=80
step=1
logfile=./log
errorfile=./error
stop_flg=0
while [ $stop_flg -ne 1 ]
	do
	echo "$(date) Step $step" >>$logfile
	for host in ${hosts[@]}
		do
		nc -zw1 $host $port >/dev/null 2>&1
		exit_code=$?
		if [ $exit_code -eq 0 ]
		then 
			echo "Host $host is available on port $port" >>$logfile
		else
			echo "Host $host is not available on port $port" >>$logfile
			echo "$host" >>$errorfile
			stop_flg=1
			break
		fi
	done
	let "step+=1"
done
```

## Дополнительное задание

`cat .git/hooks/commit-msg`

```
#!/bin/bash
COMMIT_MSG=$(head -1 $1)
CORRECT_MSG="[$(git branch | grep "*" | sed 's/* //')]"
CHAR_COUNT=$(echo $COMMIT_MSG | wc -m)
if [[ "$COMMIT_MSG" != *"$CORRECT_MSG"* ]]
	then
		echo "Commit message must contain the task code in the format [<TASK-CODE>]"
		echo "<TASK-CODE> matches development branch"
		exit 1
	elif [[ $CHAR_COUNT -gt 31 ]]
		then
			echo "Maximum 30 characters allowed in commit message"
			exit 1
fi
```