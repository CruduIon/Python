#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
#
#На ввод могут подаваться и повторяющиеся числа.
#
#Sample Input 1:
#8
#2
#14
#Sample Output 1:
#14
#2
#8
#
#Sample Input 2:
#23
#23
#21
#Sample Output 2:
#23
#21
#23



a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
    max = a
elif (b >= a and b >= c):
    max = b
else:
    max = c
if (a <= b and a <= c):
    min = a
elif (b <= a and b <= c):
    min = b
else:
    min = c
print(max)
print(min)
if ((a == max and b == min) or (b == max and a == min)):
    print(c)
elif ((a == max and c == min) or (c == max and a == min)):
    print(b)
else:
    print(a)