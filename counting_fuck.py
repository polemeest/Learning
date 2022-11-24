n = int(input())
fir = n % 10
sec = (n %100) // 10
if fir == 0:
    print(f'{n} программистов')
if fir == 1 and sec != 1:
    print(f'{n} программист')
if 2<= fir <=4 and sec != 1:
    print(f'{n} программиста')
if 5<= fir <=9 and sec != 1:
     print(f'{n} программистов')
if sec == 1 and fir != 0:
    print(f'{n} программистов')


i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)


n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))

