import unittest
import math
import main



filename = open("mainfile", "r")
strings = filename.read()
numbers = strings.split(" ")
try:
    numbers = list(map(int, numbers))
except ValueError:
    print("Файл не отвечает входным требованиям или пустой - удалите текстовые символы "
          "или запишите цифры в одну строку через пробел.")


class TestOne(unittest.TestCase):
    def test_min(self, data):
        test_min = main.mainclass.mini("")
        self.assertEqual(min(data), test_min)

    def test_max(self, data):
        test_max = main.mainclass.maxi("")
        self.assertEqual(max(data), test_max)

    def test_sum(self, data):
        test_sum = main.mainclass.summa("")
        self.assertEqual(sum(data), test_sum)

    def test_com(self, data):
        test_com = main.mainclass.comp("")
        self.assertEqual(math.prod(data), test_com)

    def test_speed(self):
        self.assertRaises()


"""
проверяющие корректность работы функций поиска минимума и максимума
проверяющие корректность работы функций сложения и умножения
проверяющие скорость работы программы при увеличении размера входного файла

"""