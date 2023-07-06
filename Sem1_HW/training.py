# # text = "Всякая записанная речь (литературное произведение, сочинение, документ и т. п., а также часть, отрывок из них)."
# #
# # def get_unicode(txt: str) -> list[int]:
# #     return sorted(list(map(ord, txt)), reverse=True)
# #
# #
# # print(get_unicode(text))
#
#
# # def unicode_dict(string: str) -> dict:
# #     st, end = map(int, string.split())
# #     res = {}
# #     for digit in range(st, end+1):
# #         res[ord(str(digit))] = digit
# #     return res
# #
# # print(unicode_dict('4 8'))
#
# def bubble_sort(lst: list[int]) -> list[int]:
#     for i in range(len(lst)):
#         for j in range(i+1):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#
#     return sorted(lst, reverse=False)
# print(bubble_sort([5, 7, 9, 10, 2, 4]))
#
# def bubble_sort2(lst: list[int]) -> list[int]:
#     return [(i, j) for i in range(len(lst)) for j in range(i+1) ]

data = [1, 3, 5, 7, 9, 11, 13, 15]

res1 = {item: item**3 for item in data if item % 3 == 0}
print(res1)
res2 = (item**3 for item in data if item % 3 == 0)
print(res2)
res2 = [item**3 for item in data if item % 3 == 0]
print(res2)