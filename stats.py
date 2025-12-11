def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        return f"Found {num_words} total words"


def num_of_char(filepath):
    char_count = {}
    with open(filepath) as f:
        file_contents = f.read().lower()
    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
