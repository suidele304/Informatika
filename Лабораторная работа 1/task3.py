list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Находим середину
middle_index = len(list_players) // 2 #Делим общее кол-во игроков пополам
#Разделяем игроков на команды используя срезы от начала и с конца
team_1 = list_players[:middle_index]
team_2 = list_players[middle_index:]
#Выводим команды
print(team_1)
print(team_2)
