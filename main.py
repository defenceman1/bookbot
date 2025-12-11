def main():
    # print("is this working???")
    get_book_text("books/frankenstein.txt")
    # print("is this working so far???")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
