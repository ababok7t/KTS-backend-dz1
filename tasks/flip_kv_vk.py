from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """"Переворачивает словарь, меняя местами ключи и значения.

  Args:
    dictionary: Словарь, который нужно перевернуть.

  Returns:
    Новый словарь, где ключи и значения поменялись местами.
  """

    return {value: key for key, value in d.items()}
print(flip_kv_vk({"a" : "b","c" : "d"}))


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """Формирует словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - список ключей,
    конфликтующих значений.

    Example:
        >> flip_kv_vk({'Санкт-Петербург': '+3', 'Москва': '+3'})
        {
            '+3': ['Москва', 'Санкт-Петербург'],
        }
    """
    # reversed_dict = {}
    # for key, value in d.items():
    #     if value not in reversed_dict:  # Избегаем дублирования ключей
    #         reversed_dict[value] = key
    #     else:
    #         # Если значение уже существует, то создаем список,
    #         # добавляем текущий ключ в список и обновляем значение.
    #         if isinstance(reversed_dict[value], list):
    #             reversed_dict[value].append(key)
    #         else:
    #             reversed_dict[value] = [reversed_dict[value], key]

    # return reversed_dict
    flipped_dict = {}
    for key, value in d.items():
        if value in flipped_dict:
            # Если значение уже есть в словаре, добавим ключ в список
            flipped_dict[value].append(key)
        else:
            # Если значение еще не встречалось, создадим список с этим ключом
            flipped_dict[value] = [key]

    return flipped_dict
