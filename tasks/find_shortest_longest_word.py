__all__ = ("find_shortest_longest_word",)
import re

def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    words = re.findall(r'\w+', text)
    if not words:  # Если список слов пуст
        return (None, None)
    shortest_word = min(words, key=len)  # Ищем самое короткое слово
    longest_word = max(words, key=len)  # Ищем самое длинное слово
    return (shortest_word, longest_word)
    raise NotImplementedError
