#Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
#
#Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
#
#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
#
#Sample Input 1:
#9 5 3
#0 7 -1
#-5 2 9
#end
#Sample Output 1:
#3 21 22
#10 6 19
#20 16 -1
#
#Sample Input 2:
#1
#end
#Sample Output 2:
#4



mat = []
while True:
    str = input()
    if str == 'end':
        break
    else:
        str = str.split()
        str = [int(i) for i in str]
        mat.append(str)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if len(mat) == 1 and len(mat[0]) != 1:
            if i == 0 and j == 0:
                print(mat[i][j+1] + mat[i][j] + mat[i][-1] + mat[i][j], end = ' ')
            elif i == 0 and j == len(mat[0])-1:
                print(mat[i][0] + mat[i][j] + mat[i][j-1] + mat[i][j], end = ' ')
            else:
                print(mat[i][j+1] + mat[i][j] + mat[i][j-1] + mat[i][j], end = ' ')
        elif len(mat) != 1 and len(mat[0]) == 1:
            if i == 0 and j == 0:
                print(mat[i][j] + mat[i+1][j] + mat[i][j] + mat[-1][j], end = ' ')
            elif i == len(mat)-1 and j == 0:
                print(mat[i][j] + mat[0][j] + mat[i][j] + mat[i-1][j], end = ' ')
            else:
                print(mat[i][j] + mat[i+1][j] + mat[i][j] + mat[i-1][j], end = ' ')
        elif len(mat) == 1 and len(mat[0]) == 1:
            print(mat[0][0] * 4)
        elif len(mat) != 1 and len(mat[0]) != 1:
            if i == 0 and j == 0:
                print(mat[i][j+1] + mat[i+1][j] + mat[i][-1] + mat[-1][j], end = ' ')
            elif i == 0 and j == len(mat[0])-1:
                print(mat[i][0] + mat[i+1][j] + mat[i][j-1] + mat[-1][j], end = ' ')
            elif i == len(mat)-1 and j == 0:
                print(mat[i][j+1] + mat[0][j] + mat[i][-1] + mat[i-1][j], end = ' ')
            elif i == len(mat)-1 and j == len(mat[0])-1:
                print(mat[i][0] + mat[0][j] + mat[i][j-1] + mat[i-1][j], end = ' ')
            elif i == 0 and j != 0 and j!= len(mat[0])-1:
                print(mat[i][j+1] + mat[i+1][j] + mat[i][j-1] + mat[-1][j], end = ' ')
            elif i != 0 and i != len(mat)-1 and j == 0:
                print(mat[i][j+1] + mat[i+1][j] + mat[i][-1] + mat[i-1][j], end = ' ')
            elif i != 0 and i != len(mat)-1 and j == len(mat[0])-1:
                print(mat[i][0] + mat[i+1][j] + mat[i][j-1] + mat[i-1][j], end = ' ')
            elif i == len(mat)-1 and j != 0 and j!= len(mat[0])-1:
                print(mat[i][j+1] + mat[0][j] + mat[i][j-1] + mat[i-1][j], end = ' ')
            else:
                print(mat[i][j+1] + mat[i+1][j] + mat[i][j-1] + mat[i-1][j], end = ' ')
    print()