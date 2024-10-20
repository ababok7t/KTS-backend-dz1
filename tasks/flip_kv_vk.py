from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:

    return {value: key for key, value in d.items()}
print(flip_kv_vk({"a" : "b","c" : "d"}))


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    flipped_dict = {}
    for key, value in d.items():
        if value in flipped_dict:
            flipped_dict[value].append(key)
        else:
            flipped_dict[value] = [key]

    return flipped_dict
