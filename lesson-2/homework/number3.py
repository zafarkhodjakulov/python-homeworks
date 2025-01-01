# 1-yechim
number = float(input("Kilometr kiriting: "))
metr = number * 10e3
santimetr = number * 10e5
print(metr, santimetr)

# 2-yechim
number = float(input("Kilometr kiriting: "))
a = number * 1000
metr = a // 1
b = a % 100
santimetr = b // 1
print(f"Bizga berilgan {number} km, aslida {metr} metru {santimetr} santimertga teng.")