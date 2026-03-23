salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
def no_debt(capital): #Вводим функцию для проверки хватит ли нам подушки на 10 месяцев
    all_capital = capital
    current_spend = spend
    for month in range(months): #Проверяем хватит ли бюджета на расходы
        if all_capital + salary < current_spend:
            return False
        all_capital -= (current_spend - salary) #Вычитаем из подушки разницу между расходами и зарплатой
        if month < months - 1: #Увеличиваем расходы на следующий месяц
            current_spend *= (1 + increase)
    return all_capital >= 0 #В конце подушка должна быть больше 0
money = 0 #Подбираем минимальную подушку
step=0.01
while not no_debt(money):
    money += step
money=int(money) #Округляем в меньшую сторону
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money)
