def get_book_text(path: str) -> str:
    with open(path) as f:
        file_conents = f.read()
        return file_conents


def get_num_of_words(text: str) -> int:
    words = text.split(sep=None)
    return len(words)


def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_num_of_words(file_contents)
    print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
