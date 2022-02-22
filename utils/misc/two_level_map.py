from typing import List, Callable, Union


def two_level_map(list_for_map: List, func: Callable, save_struct: bool) -> Union[List[List], List]:
    """
    Данная функция предназначена для обработки массивов с глубиной 2.
    (в дальнейшем её можно сделать рекурсивной, для работы с любой глубиной)
    Параметр save_struct отвечает за сохранение структуры результата.

    Допустим, вызовем данную функцию для [[1, 2], [3, 4]] и lambda x: x ** 2
    При save_struct == True получим [[1, 4], [9, 16]]
    При save_struct == False получим [1, 4, 9, 16]

    :param list_for_map: список, который будет мапиться
    :param func: функция, которая будет применяться для каждого элемента
    :param save_struct: определяет, будет ли сохранена структура переданного списка
    :return: возвращает списки разной глубины в зависимости от save_struct
    """

    new_list = []
    for i in range(len(list_for_map)):
        if save_struct:
            new_list.append([])
            for item in list_for_map[i]:
                new_list[i].append(func(item))
        else:
            for item in list_for_map[i]:
                new_list.append(func(item))
    return new_list
