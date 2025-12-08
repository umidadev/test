a = int(input('a sonni kiriting:'))
b = int(input('b sonni kiriting:'))
c = int(input('c sonni kiriting:'))

if a == b == c:
    print("Teng tomonli")
elif a == b or b == c or a == c:
    print("Teng yonli")
else:
    print("Turli tomonli")