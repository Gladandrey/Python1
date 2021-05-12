# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого
# стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию
# и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

ROOT = os.path.dirname(__file__)
project_name = 'my_project'
paths = [os.path.join(project_name, 'settings'), os.path.join(project_name, 'mainapp'),
         os.path.join(project_name, 'adminapp'),
         os.path.join(project_name, 'authapp')]
for _path in paths:
    os.makedirs(os.path.join(ROOT, _path), exist_ok=True)
