a, b = map(int, input("Sapce tashab ikkita son kiriting: ").split())

x = bool(a + b > 50.8)
y = bool(10 < a and a < 20)
z = bool(10 < b and b < 20)

print(f"Ikki sonning yig'indisi 50.8 dan katta --- {x}\na soni 10 va 20 sonlari oralig'ida --- {y}\nb soni 10 va 20 sonlari oralig'ida --- {z}")