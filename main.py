import math, time

start = time.time()
filename = open("mainfile", "r")
strings = filename.read()
numbers = strings.split(" ")
try:
    numbers = list(map(int, numbers))
    lenght = len(numbers)
    numbers.sort()
except ValueError:
    print("Файл не отвечает входным требованиям или пустой - удалите текстовые символы "
          "или запишите цифры в одну строку через пробел.")

class mainclass:
    def __init__(self):
        pass

    def mini(self):
        minimum = numbers[0]
        return minimum

    def maxi(self):
        maximum = numbers[lenght - 1]
        return maximum

    def summa(self):
        summ = 0
        for subnumbers in numbers:
           summ += subnumbers
        return summ

    def comp(self):
        multi = 1
        for subnumbers in numbers:
            multi = multi * subnumbers
        return multi

    def output_info(self):
        print("Минимум:", mainclass.mini(""))
        print("Максимум:", mainclass.maxi(""))
        print("Сумма:", mainclass.summa(""))
        print("Произведение:", mainclass.comp(""))


mainclass.output_info('')
end = time.time()
delta = end - start
print("Скорость выполнения программы: ", delta, "секунды")

