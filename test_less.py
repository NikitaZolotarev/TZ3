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
    
    def test_min_less_max(self):
        test_min = main.mainclass.mini("")
        test_max = main.mainclass.maxi("")
        self.assertLessEqual(test_min, test_max)
