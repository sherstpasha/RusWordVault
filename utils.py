def get_dictionary(words=False, pre_reform_words=False, phrases=False):
    """
    Возвращает объединённый словарь в виде кортежа. Загрузка словарей происходит в зависимости от переданных аргументов.

    :param words: Булев параметр, указывающий, загружать ли словарь words.txt.
    :param pre_reform_words: Булев параметр, указывающий, загружать ли словарь pre_reform_words.txt.
    :param phrases: Булев параметр, указывающий, загружать ли словарь phrases.txt.
    :return: Кортеж, содержащий все слова из выбранных словарей, или предупреждение, если ни один словарь не выбран.
    """
    all_words = []

    if words:
        with open('words.txt', 'r', encoding='utf-8') as file:
            all_words.extend(file.read().splitlines())
    
    if pre_reform_words:
        with open('pre_reform_words.txt', 'r', encoding='utf-8') as file:
            all_words.extend(file.read().splitlines())
    
    if phrases:
        with open('phrases.txt', 'r', encoding='utf-8') as file:
            all_words.extend(file.read().splitlines())

    if not all_words:
        return "Предупреждение: Ни один словарь не был выбран."

    return tuple(all_words)


def get_alphabet(words=False, pre_reform_words=False, phrases=False):
    """
    Возвращает объединённый алфавит из выбранных словарей в виде множества (set).

    :param words: Булев параметр, указывающий, загружать ли алфавит для words.txt.
    :param pre_reform_words: Булев параметр, указывающий, загружать ли алфавит для pre_reform_words.txt.
    :param phrases: Булев параметр, указывающий, загружать ли алфавит для phrases.txt.
    :return: Множество, содержащее все уникальные символы (алфавит) из выбранных словарей, или предупреждение, если ни один словарь не выбран.
    """
    all_characters = set()

    if words:
        with open('words.txt', 'r', encoding='utf-8') as file:
            all_characters.update(file.read())

    if pre_reform_words:
        with open('pre_reform_words.txt', 'r', encoding='utf-8') as file:
            all_characters.update(file.read())

    if phrases:
        with open('phrases.txt', 'r', encoding='utf-8') as file:
            all_characters.update(file.read())

    # Удаляем символы новой строки, так как они не должны учитываться в алфавите
    all_characters.discard('\n')

    if not all_characters:
        return "Предупреждение: Ни один словарь не был выбран."

    return all_characters
