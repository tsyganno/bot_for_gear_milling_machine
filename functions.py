def find_combinations(shesterni, tochnost, u, results_limit):
    printed_combinations = set()
    results_count = 0
    for a in shesterni:
        for b in shesterni:
            for c in shesterni:
                for d in shesterni:
                    if (a != b and a != c and a != d and b != a and b != c and b != d and c != a and c != b and c != d and d != a and d != b and d != c) and (a + b <= 140) and (c + d >= 110) and (a >= 30 or a > 18):
                        alfa = a * c
                        beta = b * d
                        module = round(alfa / beta, tochnost)
                        if module % u == 0:
                            if module == u:
                                q = [a, b, c, d]
                                combination = tuple(q)
                                if combination not in printed_combinations:
                                    print("A= ", q[0], "B= ", q[1], "C= ", q[2], "D= ", q[3],)
                                    printed_combinations.add(combination)
                                    results_count += 1
                                    if results_count >= results_limit:
                                        return


#shesterni = list(range(20,104))
shesterni = [24, 25, 30, 30, 45, 46, 47, 48, 50, 50, 54, 55, 55, 55, 57, 59, 60, 60, 62, 64, 69, 72, 72, 80, 85, 90, 92, 95]
z = int(input("Введите количество зубов детали: "))
tochnost = int(input("Введите степень точности, количество знаков после запятой: "))
absolut = int(input("Введите постоянную делительную станка: "))
result_parametrs = int(input("Введите количество результатов: "))
u = absolut / z
u_rounded = round(u, tochnost)
find_combinations(shesterni, tochnost, u_rounded, result_parametrs)
