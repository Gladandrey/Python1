# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
#
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
# Вариант решения с yaml
# config.yaml
# my_project:
# - settings:
#   - __init__.py
#   - dev.py
#   - prod.py
# - mainapp:
#   - __init__.py
#   - models.py
#   - views.py
#   - templates:
#       - mainapp:
#           - base.html
#           - index.html
# - authapp:
#   - __init__.py
#   - models.py
#   - views.py
#   - templates:
#       - authapp:
#           - base.html
#           - index.html


import os

HOME = os.path.split(os.path.abspath(__file__))[0]
list_dirs = {
    'my_project': [{'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}, 'settings', 'mainapp', 'adminapp',
                   'authapp', 'test.txt']}

list_dirs2 = ['settings', 'mainapp', 'adminapp', 'authapp']


def make_dirs(path, list_dir):
    work_dir = path
    for i in list_dir:
        try:
            os.mkdir(i)
        except FileExistsError:
            print(f'folder {i} is already exists in directory {work_dir}')

        if type(list_dir) is dict:
            for j in list_dir[i]:
                work_dir = os.path.join(path, i)
                os.chdir(work_dir)
                if type(j) is dict:
                    make_dirs(work_dir, j)
                else:

                    if len(j.split('.')) == 2:
                        try:
                            with open(j, 'w+', encoding='utf-8') as file:
                                file.close()
                        except FileExistsError:
                            print(f'file {j} is already exists in directory {work_dir}')
                    else:
                        try:
                            os.mkdir(j)
                        except FileExistsError:
                            print(f'folder {j} is already exists in directory {work_dir}')


if __name__ == '__main__':
    make_dirs(HOME, list_dirs)

