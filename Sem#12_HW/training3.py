from string import punctuation

# def longest_word_in_file(filename: str):
#     result = ''
#     with open(filename, 'r', encoding='utf-8') as file:
#         for word in file.readline().split():
#             for sign in punctuation:
#                 if sign in word:
#                     word = word.replace(sign, '')
#                 if len(word) >= len(result): result = word
#     return result
#
#
# print(longest_word_in_file('test.txt'))

with open('test.txt', 'r', encoding='utf-8') as file:
    data = file.readline()
        for sign in punctuation:
            if sign in word:
    #             word = word.replace(sign, '')
    #             print(word)