# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.

requests_dict = {}

with open('new_file.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        requests_dict[line[0]] = requests_dict.get(line[0]) + 1 if requests_dict.get(line[0]) != None else 1

spamers_dict = sorted(requests_dict, key=requests_dict.get, reverse=True)

print(f'Spammer: {spamers_dict[0]}, requests: {requests_dict.get(spamers_dict[0])}')
