# Matriz 5x5
matriz_5x5 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
print(matriz_5x5[0])
print(matriz_5x5[1])
print(matriz_5x5[2])
print(matriz_5x5[3])
print(matriz_5x5[4])

for lista in matriz_5x5:
    for item in lista:
        if (item % 2) == 0:
            print(f' Este é o número é Par: {item}')
        elif item == 5:
            print(f'Este é  o número cinco: {item}')
        elif(item %2) != 0:
            print(f' Este número não é cinco e é ímpar:{item}')