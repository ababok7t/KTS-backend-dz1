__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """

    if len(numbers) == 0:
        return 0
    se = 0
    so = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            se += numbers[i]
        else:
            so += numbers[i]
    if se == 0 or so == 0:
        return 0
    return se / so

    raise NotImplementedError
