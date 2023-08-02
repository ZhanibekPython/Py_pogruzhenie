import os
import pickle


def search_and_pickle(extention: str = 'json'):
    files = list(filter(lambda x: x.endswith(extention), os.listdir()))
    for name in files:
        root_ext = os.path.splitext(name)
        with (
            open(name, 'r') as reading,
            open(name + '.pickle', 'wb') as file
        ):
            info = reading.read()
            pickle.dump(file=file, obj=info)


with open('users_1.json.pickle', 'rb') as source:
    my_dict = pickle.load(source)
for key, value in my_dict.items():
    list = []
    in root_ext = os.path.splitext()
print(my_dict)