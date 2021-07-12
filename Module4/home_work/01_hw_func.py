# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых трех и последних трех цифр равны.

def lucky_ticket(ticket_number):
    sum_before = int(str(ticket_number)[:1]) + int(str(ticket_number)[1:2])
    sum_after = int(str(ticket_number)[-1]) + int(str(ticket_number)[-2])
    return sum_before == sum_after


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
