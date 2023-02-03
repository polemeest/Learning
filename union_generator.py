 summ = set()
 for i in range(int(input())):
     summ.update(input().split())
 print(len(summ))

print(len(set.union(*({*input().split()} for _ in range(int(input()))))))