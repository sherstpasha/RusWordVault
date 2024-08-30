def get_dictionary(pre_reform=False):
    """
    Возвращает весь словарь в виде кортежа. Если pre_reform=True, загружается словарь pre_reform_words.txt.
    В противном случае загружается словарь words.txt.

    :param pre_reform: Булев параметр, указывающий, какой словарь загрузить. 
                       Если True, загружается pre_reform_words.txt, иначе words.txt.
    :return: Кортеж, содержащий все слова из выбранного словаря.
    """
    file_name = 'pre_reform_words.txt' if pre_reform else 'words.txt'
    
    with open(file_name, 'r', encoding='utf-8') as file:
        words = tuple(file.read().splitlines())
    
    return words

def get_alphabet(pre_reform=False):
    """
    Возвращает алфавит, использующийся в словаре. Если pre_reform=True, загружается алфавит для pre_reform_words.txt.
    В противном случае загружается алфавит для words.txt.

    :param pre_reform: Булев параметр, указывающий, какой алфавит загрузить. 
                       Если True, используется алфавит для pre_reform_words.txt, иначе для words.txt.
    :return: Кортеж, содержащий все уникальные символы (алфавит) из выбранного словаря.
    """
    file_name = 'pre_reform_words.txt' if pre_reform else 'words.txt'
    
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        alphabet = tuple(sorted(set(content.replace('\n', ''))))  # Уникальные символы без учета переносов строк
    
    return alphabet



import pandas as pd

def split_and_save_to_excel(input_file, chunk_size=5000):
    """
    Разбивает файл на куски по определенному количеству строк и сохраняет их в отдельные строки Excel.

    :param input_file: Путь к текстовому файлу.
    :param chunk_size: Количество строк в каждом куске (по умолчанию 5000).
    """
    # Чтение всех строк из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Определение количества чанков
    num_chunks = (len(lines) + chunk_size - 1) // chunk_size

    # Создание Excel writer
    excel_file = input_file.replace('.txt', '.xlsx')
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

    # Разделение и сохранение в разные строки Excel
    chunked_lines = [
        ''.join(lines[i * chunk_size:(i + 1) * chunk_size])
        for i in range(num_chunks)
    ]
    df = pd.DataFrame(chunked_lines, columns=['Phrases'])
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Сохранение Excel файла
    writer.save()
    print(f"Файл сохранен как {excel_file}")

# Пример использования функции
input_file_path = 'phrases.txt'  # Укажите путь к вашему файлу phrases.txt
split_and_save_to_excel(input_file_path)


