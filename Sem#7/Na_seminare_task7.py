from os import listdir, mkdir, chdir
from pathlib import Path


# task_7

def get_exts(exts: list[str]) -> list[str]:
    exts = set(map(lambda x: x.split('.')[-1], exts))
    return list(exts)

def sort_files(working_dir: str = 'For_task4'):
    exts = get_exts(listdir(Path(working_dir)))
    chdir(Path(working_dir))
    for ext in exts:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    print(listdir())
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)

sort_files()