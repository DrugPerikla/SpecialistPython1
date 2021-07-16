# Чтобы	поднять холодильник на n-й этаж H-этажного дома, Коля вызвал бригаду грузчиков.
# За подъем холодильника на один этаж требуется заплатить 200 рублей, за спуск на один этаж — 100 рублей.
# За подъем и спуск на лифте плата не взимается.
# Несмотря на то, что в Колином доме есть лифт, ему возможно все же придется заплатить грузчикам,
# поскольку лифт останавливается только на каждом K-м этаже, начиная с первого
# (то есть на этажах с номерами 1, K+1, 2K+1, 3K+1, …).
# Требуется вычислить, за какую минимальную сумму грузчики доставят холодильник с первого этажа на этаж Коли.

# Формат входных данных
# Даны три числа, H - высота дома, N - этаж Коли и k - через сколько этажей останавливается лифт.
# H (2≤H≤100), n (2≤n≤H) и K (2≤k≤H–1).
# Формат выходных данных
# Выведите одно целое число - минимальную стоимость подъема

# Примеры для самопроверки:
# Входные данные-1:
# 20
# 7
# 4
# Выходные данные-1:
# 200
# Входные данные-2:
# 20
# 7
# 2
# Выходные данные-2:
# 0
H = int(input("Введите высоту дома: "))
N = int(input("Введите этаж Коли: "))
k = int(input("Введите сколько этажей останавливается лифт: "))

price_up = 200
price_down = 100

k_list = range(1, H, k) # список этажей остановок
price = min([price_up*(N - x) if x <= N else (x - N)*price_down for x in k_list])

print("Mинимальная стоимость подъема: ", price)
