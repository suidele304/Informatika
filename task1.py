def find_item_index(items, target): #Создаем функцию с двумя параметрами и перебираем список с индексами
    for index, item in enumerate(items):
        if item == target: #Если нашли нужный товар то возвращаем его индекс, если не нашли то возвращаем None
            return index
    return None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item) #Вызываем функцию, получаем индекс или None
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
