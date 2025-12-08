harf = input('Harf kiriting: ')

katta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kichik = "abcdefghijklmnopqrstuvwxyz"

if harf in katta:
    print('Katta harf')
elif harf in kichik:
    print("Kichik harf")
else:
    print("Harf emas")
