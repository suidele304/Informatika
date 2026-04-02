import json
import csv
source_data = "input.csv"
result_json = "output.json"
def convert_csv_to_json(): #Читаем исходный csv-файл
    with open(source_data) as f_in: #Превращаем каждую строку в словарь DictReader, а потом сразу в список
        data_list = [row for row in csv.DictReader(f_in)] #Записываем результат в json
    with open(result_json, 'w') as f_out: #Красиво форматируем с отступами
        json.dump(data_list, f_out, indent=4)
if __name__ == "__main__": #Запускаем основную функцию
    convert_csv_to_json()
with open(result_json) as f_result:
    for line in f_result:
        print(line, end="")
