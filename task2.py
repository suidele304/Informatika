def find_common_participants(group1, group2, delimiter = ","): #Разбираем строки на списки
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    for i in range(len(list1)): #Убираем пробелы вокруг фамилий
        list1[i] = list1[i].strip()
    for i in range(len(list2)):
        list2[i] = list2[i].strip()
        common = [] #Ищем общих участников
        for name1 in list1:
            for name2 in list2:
                if name1 == name2 and name1 not in common:
                    common.append(name1)
        common.sort() #Сортируем список
        return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, " | ") #Проверяем работу функции с разделителем |
print("Общие участники:", result)