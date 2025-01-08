def invest(amount, rate, years):
    amount_list = []
    for i in range(years):
        amount += amount / 100 * rate
        amount_list.append(round(amount, 2))
    for j in range(years):
        print(f"year {j + 1}: ${amount_list[j]:.2f}")
print(invest(100, 5, 4))