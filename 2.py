#Требуется найти в массиве A[1...N] самый близкий по величине элемент к заданному числу X. Пользователь
#в первой строке вводит натуральное число N- количество элементов в массиве. В последующих строках записаны
#N целых чисел Ai. последняя строка содержит число X.
N = int(input("ВВедите количество элементов в массиве: "))
list= [int(input()) for i in range (N)]
print (list)
X = int(input("ВВедите искомое число: "))
min = abs (list[0]-X)
num = list[0]
for i in list:
    if abs(i-X)<min:
        min = abs(i-X)
        num = i
print(num)

