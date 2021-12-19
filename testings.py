import unittest
import math
import main



filename = open("mainfile", "r")
strings = filename.read()
data = strings.split(" ")
try:
    data = list(map(int, data))
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
        test_time_one = main.delta
        test_time_two = 0.0003657341003417969
        self.assertAlmostEqual(test_time_two, test_time_one, "Несовпадение")

    def test_min_less_max(self):
        test_min = main.mainclass.mini("")
        test_max = main.mainclass.maxi("")
        self.assertLessEqual(test_min, test_max)
