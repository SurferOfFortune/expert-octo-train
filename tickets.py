tickets_cost = [] 
wanted_ticket = int(input('Сколько билетов вы хотите купить? '))
for i in range(wanted_ticket):
   age = int(input('Введите возраст посетителя  '))
   if age < 18:
       tickets_cost.append(0)
   if age >= 18 and age < 25:
       tickets_cost.append(990)
   if age > 25:
    tickets_cost.append(1390)
   if wanted_ticket > 3:
      result =  (sum(tickets_cost))-((sum(tickets_cost))*0.1)
   else:
      result = (sum(tickets_cost))
print (int(result))