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

    def test_speed(self):
        test_time_one = main.delta
        test_time_two = 0.0003657341003417969
        self.assertAlmostEqual(test_time_two, test_time_one, "Несовпадение")
