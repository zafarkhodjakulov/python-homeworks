a, b = map(float, input("Ikkita son kiriting bo'sh joy tashlab: ").split())
number = divmod( a, b)
print(f"Berilgan ikkita sonning bo'lish natijasida butun qismi {number[0]}, qoldiq qismi {number[1]}")