import math

c = int(input('サイクルタイムを入力してください'))
d = int(input('要素作業数を入力してください'))
t = 0

for i in range(0,d):
    t += int(input('数値を入力してください'))

result = (t/c + 1)
n = math.floor(result)
print('作業者数Nは' + str(n))
e = t/(n*c) * 100
print('E=' + str(e))
