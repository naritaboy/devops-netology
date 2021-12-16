# devops-netology
# Modified

terraform/.gitignore

Будут игнорироваться при коммите следующие файлы в папке terraform
- файлы с названием crash.log, override.tf, override.tf.json, .terraformrc, terraform.rc
- файлы с расширением .tfstate и .tfvars
- файлы, название которых заканчивается на _override.tf и _override.tf.json
- файлы, название которых начинается на crash. и имеют расширение .log
- файлы, в названии которых содержится .tfstate.
- все файлы в каталоге и подкаталоге .terraform

New line PyCharm