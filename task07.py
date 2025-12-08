email = input( 'Emaillingizni kiriting: ')

if "@" in email and "." in email and " " not in email and email.index("@") < email.rindex("."):
    print("Email manzili to'g/'ri")
else:
    print("Email manzili noto'g/'ri")