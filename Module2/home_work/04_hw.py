# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######
a=int(input("Введите размер строрны квадрата:"))
print ("#"*a)
i=1
while i < (a-1):
    print("#","*"*(a-2),"#")
    i+=1
print("#"*a)
