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