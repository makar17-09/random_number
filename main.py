from random import randint

num=randint(10,99)
my_num=int(input('введите число '))
if num== my_num:
    print('УРА! Ты угадал ')
else:
    print('ты не угадал ')
    print('загаданое число ',num)


