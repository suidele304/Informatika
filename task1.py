import json
FILENAME = "input.json"
def task() -> float: #Открываем json файл с данными
    with open(FILENAME) as file: #Загружаем содержимое в обьект
        raw_data = json.load(file)
        multiplied = [d["score"]*d["weight"] for d in raw_data] #Умножаем score на weight для каждого элемента
        result_sum = sum(multiplied) #Складываем все в месте
        return round(result_sum,3) #Возвращаем с округлением до трех знаков после запятой
print(task())
