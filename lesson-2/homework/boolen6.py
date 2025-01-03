number = int(input('Birorta son kiriting: '))

x = not bool(number % 3)
y = not bool(number % 5)
z = not bool(number % 15)

print(x, y, z)