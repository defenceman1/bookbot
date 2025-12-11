def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        return f"Found {num_words} total words"
