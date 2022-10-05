import numpy as np


def smart_predict(x: int, verh: int = 100, niz: int = 1) -> int:
    """ Угадываем средним границ отрезка

    Args:
        x (int): число, которое угадываем.
        verh (int, optional): верхняя граница отрезка угадывания. Defaults to 100.
        niz (int, optional):нижняя граница отрезка угадывания. Defaults to 1.

    Returns:
        int: число попыток для угадывания
        
    number - начальная точка, середина отреза
    count - счетчик
    """
    number = (verh+niz)//2 
    count = 3
    if x == verh :
        return 1
    if x == niz:
        return 2
    while number != x:
        count += 1
        if number > x:
            verh = number
        elif number < x:
            niz = number
        number = (verh + niz + 1)//2
    return count