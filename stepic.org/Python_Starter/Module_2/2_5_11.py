#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
#
#Для решения задачи может пригодиться метод sort списка.
#
#Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
#
#Sample Input 1:
#4 8 0 3 4 2 0 3
#Sample Output 1:
#0 3 4
#
#Sample Input 2:
#10
#Sample Output 2:
#
#Sample Input 3:
#1 1 2 2 3 3
#Sample Output 3:
#1 2 3
#
#Sample Input 4:
#1 1 1 1 1 2 2 2
#Sample Output 4:
#1 2



a = [int(i) for i in input().split()]

cnt = 1
a.sort()
for i in range(len(a)):
    if i == len(a) - 1:
        if cnt > 1:
            print(a[i], end = ' ')
    elif a[i] == a[i + 1]:
        cnt += 1
    elif cnt > 1 and a[i] != a[i + 1]:
        print(a[i], end = ' ')
        cnt = 1
    else:
        cnt = 1