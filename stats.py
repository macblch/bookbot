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


def sort_chars_dict(char_dict: dict[str[int]]) -> list[dict[str[int]]]:
    dict_list = []

    for key in char_dict:
        new_dict = {}

        if not key.isalpha():
            continue

        new_dict["char"] = key
        new_dict["num"] = char_dict[key]

        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def sort_on(items):
    return items["num"]
