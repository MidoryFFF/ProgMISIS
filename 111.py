


###25+
###17928493 5309
###27958183 8279
###67908093 20109
##from itertools import product
##sp = []
##for x in range(10):
##    for y in range(10):
##        for j in range(3):
##            for z in product('0123456789', repeat = j):
##                z = ''.join(z)
##                if int(f'{x}79{y}8{z}3') % 3377 == 0:
##                    sp.append([int(f'{x}79{y}8{z}3'), int(f'{x}79{y}8{z}3') // 3377])
##for i in sorted(sp):
##    print(*i)


#24-


###23+
###1692
##def f(x, y):
##    if x == y: return 1
##    if x > y or x == 21: return 0
##    if x < y:
##        return f(x + 2, y) + f(x + 3, y) + f(x * 5, y)
##print(f(1, 6) * f(6, 35))


#22-


#21-



#20-



#19-
#26


#18+
#530 128


###17+
###330 452
##with open('S:\\Подготовка к ЕГЭ информатика 2024\\Файлы\\17/17var04.txt') as f:
##    a = [int(i) for i in f.readlines()]
##    k = 0
##    mi = 100_000
##    mi1 = 300_000
##    for i in a:
##        if str(i)[-3:] == '700':
##            mi = min(i, mi)
##    
##    for i in range(len(a) - 2):
##        g = [str(len(str(abs(a[i])))), str(len(str(abs(a[i + 1])))), str(len(str(abs(a[i + 2]))))]
##        if g.count('5') <= 2 and a[i] + a[i + 1] + a[i + 2] >= mi:
##            k += 1
##            mi1 = min(a[i] + a[i + 1] + a[i + 2], mi1)
##print(k, mi1)


###16+
###4102638
##sp = [0] * 2025
##sp[1] = 1
##sp[2] = 2
##for n in range(3, 2025):
##    sp[n] = n * (n - 1) + sp[n - 1] - sp[n - 2]
##print(sp[2024] + sp[2020] - sp[2019])
##
##import sys
##sys.setrecursionlimit(1_000_000)
##def f(n):
##    if n == 1: return 1
##    if n == 2: return 2
##    if n > 2:
##        return n * (n - 1) + f(n - 1) - f(n - 2)
##print(f(2024) + f(2020) - f(2020))


###15+
###19
##for A in range(1000):
##    f = 1
##    for x in range(500):
##        for y in range(500):
##            if not((x >= 20) or (y >= 40) or (y <= (x + A)) or (y >= (x * 3 - A))) or (not(f)):
##                f = 0
##                break
##    if f:
##        print(A)
##        break


###14+
###3632718098
##m1 = ''
##for x in '0123456789ABCDEFGHI':
##    if (int(f'3{x}2{x}1{x}0{x}1', 19) + int(f'{x}2024', 19) + int(f'1{x}077', 19)) % 18 == 0:
##        m1 = (int(f'3{x}2{x}1{x}0{x}1', 19) + int(f'{x}2024', 19) + int(f'1{x}077', 19)) // 18
##print(m1)


#13-


###12+
###187
##for n in range(3, 10000):
##    x = '4' + '1' * n
##    while '31' in x or '411' in x or '1111' in x:
##        if '31' in x:
##            x = x.replace('31','1', 1)
##        if '411' in x:
##            x = x.replace('411', '13', 1)
##        if '1111' in x:
##            x = x.replace('1111', '4', 1)
##    x = [int(i) for i in x]
##    if sum(x) == 34:
##        print(n)
##        break


#11+
#441


#10+
#35


#9+
#8


###8-
###4320
##from itertools import product
##k = 0
##c = 0
##for i in product('АГЕИЛНР', repeat = 5):
##    c += 1
##    if c%2 != 0:
##        if i[0] != 'Т' and 1 <= i.count('Н') <= 2:
##            k += 1
##print(k)


#7+
#4480


#6-


###5+
###68
##def f(n):
##    s = ''
##    while n:
##        s = str(n%4) + s
##        n //= 4
##    return s
##
##for i in range(1, 1000):
##    r = f(i)
##    if i%4 == 0:
##        r += r[-2:]
##    elif i%4 != 0:
##        r += f(i%4 * 2)
##    if int(r, 4) >= 1088:
##        print(i)
##        break


#4+
#13


#3-
#9


###2+
###yzxw
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                if not(not(w <= x) or ((not(z)) <= (not(y))) or z):
##                    print(x, y, z, w)


#1+
##34
