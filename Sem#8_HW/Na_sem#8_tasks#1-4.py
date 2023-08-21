import json


def users_json(filename: str = 'users.json'):
    while True:
        try:
            with open(filename, 'r') as src:
                data = json.load(src)
        except FileNotFoundError:
            data = {str(i): [] for i in range(1, 8)}
        name = input('Ваше имя: ')
        id_ = input('Ваш личный идентификатор: ')
        access = input('Ваш уровень доступа: ')

        data[access].append({'name': name, 'id': id_})

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)


def json_to_csv(src_file: str = 'users.json',
                out_file: str = 'users.csv'):
    with open('users.json', 'r') as src:
        data = json.load(src)

    with open('users.csv', 'w') as res:
        res.write('id,level,name')
        for level, users_lst in data.items():
            for user in users_lst:
                res.write(f'\n{user["id"]},{level},{user["name"]}')

def csv_to_json(src_file: str='users.csv',
                out_file: str='users_1.json'):
    with open('users.csv', 'r') as src:
        data = list(map(lambda x: x.split(','), src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][2] = data[i][0].zfill(10)
        data[i][0] = data[i][2].capitalize()
        data[i].append(hash(data[i][0] + data[i][2]))

    data = data[1::]

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data]

    with open ('users_1.json', 'w') as res:
        json.dump(data, res, indent=5)
