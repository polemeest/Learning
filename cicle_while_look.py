a = int(input())
b = int(input())

min_d = 1
d = a * min_d

while d % a != 0 or d % b != 0: # опять пока while не дало false, то есть пока выражения не стали равны нулю.
    d = a * min_d
    min_d += 1
print(d)



a = int(input())
b = int(input())
d = a
while d%b: # Пока d % b даёт остаток, выражение верно, а значит while = true, значит будет выполняться. при остатке 0 while = false, а значит выполняться не будет.
    d += a
print(d)