from stats import get_num_of_chars, get_num_of_words


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_conents = f.read()
        return file_conents


def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_num_of_words(file_contents)
    chars_dict = get_num_of_chars(file_contents)

    print(f"Found {num_words} total words")
    print(chars_dict)


if __name__ == "__main__":
    main()
