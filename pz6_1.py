# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
#nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', encoding='utf-8') as f:
    with open('new_file.txt', 'a', encoding='utf-8') as a:
        for line in f:
            new_line = line.strip().split()[0:7]
            list_line = (new_line[0], new_line[5].strip('"'), new_line[6])
            a.write(' '.join(list_line) + "\n")