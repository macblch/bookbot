def get_book_text(path) -> str:
    with open(path) as f:
        file_conents = f.read()
        return file_conents


def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    print(file_contents)


if __name__ == "__main__":
    main()
