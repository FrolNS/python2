#  Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
n = input()
newn = n.split(".")
left = int(newn[0])
right = int(newn[1])
count = 0
while left != 0:
    digit = left % 10
    count = count + digit
    left = left // 10
while right != 0:
    digit = right % 10
    count = count + digit
    right = right // 10
print(count)
