phone_number = input ('Telefon raqamini kiriting: ')
kod = phone_number[:2]

if kod == "90" or kod == "91":
    print("Ucell")
elif kod == "93" or kod == "94":
    print("Beeline")
elif kod == "95" or kod == "97":
    print("Uzmobile")
elif kod == "88" or kod == "99":
    print("Mobiuz")
else:
    print("Noma/'lum operator")