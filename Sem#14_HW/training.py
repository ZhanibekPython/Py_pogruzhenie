import re


def correct_text(text: str) -> str:
    """
    Return only the Latin alphabet chors and probels
    >>> correct_text("Access ERROR проверка BLA-bla")
    access error  blabla
    >>> correct_text('HI hi пвщпщв WORLD')
    hi hi  world
    """
    return re.sub(r'[^a-zA-Z ]', '', text).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

# class TestCorrectText(unittest.TestCase):
#     def test_text(self):
#         self.assertEqual('Hello WORLD'.lower(), correct_text('Hello WORLD'))
#
#     def test_correct_test(self):
#         self.assertEqual('hello world', correct_text('hello world'))
#
#     def test_text_punced(self):
#         self.assertEqual('hello world', correct_text('hello world!!!@#'))
#
#     def test_text_notLatin(self):
#         self.assertEqual('hello world', correct_text('hello world'))
#
#     def test_фдд(self):
#         self.assertEqual('hello world', correct_text('hello world'))
#
#
# if __name__ == '__main__':
#     unittest.main()
