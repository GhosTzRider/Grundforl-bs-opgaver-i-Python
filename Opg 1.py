sum_of_numbers = 0

for i in range(1001):
    if i % 10 == 7:
        sum_of_numbers += i
        print(i)
        print("Summen af alle tal fra 0 til 1000, der slutter pÃ¥ 7, er:", sum_of_numbers)