import pytest
import re
def correct_text(text: str) -> str:
    """Return only the Latin alphabet chors and probels"""

    return re.sub(r'[^a-zA-Z ]', '', text).lower()


def check_test():
    assert 'hello world' == correct_text('hello world')

def check_register():
    assert 'hello world' == correct_text('HeLlO WoRlD')

def check_puncs():
    assert 'hello world' == correct_text('$.,hello$#@ *world^%&')

def check_lat_alphabet():
    assert 'hello world' == correct_text('ШпшкдомщыщвоhelloААОРАОУыосмт ОУМworldлвтмлтЛТА')

def check_everything():
    assert 'hello world' == correct_text('/./657домщыщвоhelloААОРАОУыосмт., ОУМworldлвтмлтЛТА')



def test_text():
    assert 'hello world' == correct_text('Hello Worlовшоммd')
    assert 'hello world' == correct_text('hello 32зплвпзывworld')

if __name__ == '__main__':
    pass