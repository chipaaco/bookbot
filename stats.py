def get_num_words():
    word_number = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for word in file_contents.split():
        word_number += 1
    print(f"Found {word_number} total words")
