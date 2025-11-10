import sys

from stats import get_num_of_chars, get_num_of_words, sort_chars_dict


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_conents = f.read()
        return file_conents


def print_book_report(path: str, word_count: int, char_dict_list: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_dict_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file_contents = get_book_text(path)
    num_words = get_num_of_words(file_contents)
    chars_dict = get_num_of_chars(file_contents)

    sorted = sort_chars_dict(chars_dict)
    print_book_report(path=path, word_count=num_words, char_dict_list=sorted)


if __name__ == "__main__":
    main()
