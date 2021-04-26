# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
import json

with open('users.csv', encoding='utf-8') as u:
    users = u.readlines()

with open('hobby.csv', encoding='utf-8') as h:
    hobbys = h.readlines()


def users_hobby_dict(users, hobbys):
    users_hobby = {}
    for user, hobby in zip(users, hobbys):
        hobby = hobby.strip().split(",") if hobby != None else None
        users_hobby[' '.join(user.strip().split(","))] = hobby

    with open('users_hobby_6_3.json', 'w', encoding='utf-8') as uh:
        uh.write(json.dumps(users_hobby))

    with open('users_hobby_6_3.json', 'r', encoding='utf-8') as uh:
        check = json.loads(uh.read())
        print(type(check), check, sep='\n')


if (len(users) >= len(hobbys)):
    add_none = [None for i in range(0, len(users) - len(hobbys))]
    hobbys.extend(add_none)
    users_hobby_dict(users, hobbys)
elif (len(users) < len(hobbys)):
    users_hobby_dict(users, hobbys)

exit(1)
