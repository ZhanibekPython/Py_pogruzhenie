class Triangle:

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def check_sides(self):
        if self.side_a > self.side_b + self.side_c or self.side_b > self.side_a + self.side_c or self.side_c > self.side_a + self.side_b:
            return f'Такого треугольника не бывает!'
        elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
            return 'Треугольник равнобедренный'
        elif self.side_a != self.side_b != self.side_c:
            return 'Треугольник разносторонний'


# chk1 = Triangle(3, 4, 5)
# print(chk1.check_sides())

class Find_10_maxlen_words:

    def __init__(self, text):
        self.text = text

    def word_finder(self):
        self.search = {i.lower(): self.text.count(i) for i in self.text.split() if i.isalpha() and len(i) > 2}
        self.sorted_list = list(sorted(self.search.items(), key=lambda item: item[1]))
        return self.sorted_list[-10:][::-1]


finder1 = Find_10_maxlen_words('oksjdjgoksndng ookdsnfasasasasasasa ojojfnadnfkandfoakn aknslkans laskn lksk')
print(finder1.word_finder())