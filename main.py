def calculate_factorial(n):
    nFact = 1
    for i in range(n):
        nFact *= (i + 1)
    return nFact


# Первый метод
def get_result_by_int(nFact):  # Данный метод не работает с большими числами
    ctr = 0
    while nFact % 10 == 0:
        nFact /= 10
        ctr += 1
    return ctr


# Второй метод
def get_result_by_str(nFact):
    ctr = 0
    nFact = str(nFact)
    for i in nFact[::-1]:
        if i == '0':
            ctr += 1
        else:
            break
    return ctr


if __name__ == '__main__':
    n = int(input("Input n: "))
    nFact = calculate_factorial(n)
    print(f'{n}! = {nFact}')

    print(f"1st Result: {get_result_by_int(nFact)}")
    print(f"2nd Result: {get_result_by_str(nFact)}")
