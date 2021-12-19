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

    def test_com(self, data):
        test_com = main.mainclass.comp("")
        self.assertEqual(math.prod(data), test_com)
