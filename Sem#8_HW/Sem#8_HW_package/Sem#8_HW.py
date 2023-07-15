import csv
import json
import os
import pickle
import sys

dct = {}

def dict_to_all(path: str = 'D:\Check'):
    global dct
    for i in os.listdir(path):
        size_ = sys.getsizeof(path + '\\' + i)
        parent = os.path.dirname(path + '\\' + i)
        if os.path.isfile(path + '\\' + i):
            dct[i] = {'name': i, 'parent': parent, 'type': 'file', 'size': size_}
        elif os.path.isdir(path + '\\' + i):
            dct[i] = {'name': i, 'type': 'dir', 'size': size_}
            dict_to_all(path + '\\' + i)

    with open('out_pickle', 'wb') as pickle_writer:
        pickle.dump(dct, pickle_writer)
    with open('out_json', 'w') as json_:
        json.dump(dct, json_, indent=4)
    with open('out_csv', 'w', newline='', encoding='utf-8') as csv_w:
        csv_write = csv.DictWriter(csv_w, fieldnames=['name', 'parent', 'type', 'size'],
                                   dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        info = []
        for i in dct.values():
            info.append(i)
        csv_write.writerows(info)


