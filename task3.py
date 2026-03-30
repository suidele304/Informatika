def count_letters(raw_text):
    letter_stats = {}
    for position, symbol in enumerate(raw_text):
        if symbol.isalpha():
            current_letter = symbol.lower()
            # Добавляем отступ здесь, чтобы строка была внутри if
            letter_stats[current_letter] = letter_stats.get(current_letter, 0) + 1
    # return должен быть на уровне for
    return letter_stats

def calculate_frequency(letter_data):
    total_letters = sum(letter_data.values())
    # Проверка на пустой текст, чтобы не делить на ноль
    if total_letters == 0:
        return {}
    frequency_dict = {letter: round(count / total_letters, 4)
                      for letter, count in letter_data.items()}
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

raw_counts = count_letters(main_str)
frequency_results = calculate_frequency(raw_counts)

# Исправлено имя переменной с frequencies на frequency_results
for letter, freq in frequency_results.items():
    print(f"{letter}: {freq:.2f}")