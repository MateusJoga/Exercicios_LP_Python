a = int(input(''))
b = int(input(''))
c = int(input(''))

if a > b > c:
    print(f'{a} {b} {c}')
elif a > c > b:
    print(f'{a} {c} {b}')
elif b > a > c:
    print(f'{b} {a} {c}')
elif b > c > a:
    print(f'{b} {c} {a}')
elif c > a > b:
    print(f'{c} {a} {b}')
else:
    print(f'{c} {b} {a}')