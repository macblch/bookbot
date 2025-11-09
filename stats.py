def get_num_of_words(text: str) -> int:
    words = text.split(sep=None)
    return len(words)


def get_num_of_chars(text: str) -> dict[str[int]]:
    chars_count = {}

    for char in text:
        lowercased = char.lower()
        if char.lower() in chars_count:
            chars_count[lowercased] += 1
        else:
            chars_count[lowercased] = 1

    return chars_count
