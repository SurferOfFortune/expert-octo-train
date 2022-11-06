per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 
money = int(input('Введите сумму: ')) 
deposit = []                            # Объявил депозиты в список
for value in per_cent.values():         # Создал цикл  для вычисления процентов
    result = int(money/100*value)
    deposit.append(result)              # Полученный результат записывается в список deposit
print(deposit)
print(max(deposit))                     # Вывожу максимальное значение списка
