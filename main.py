def get_book_text():
    word_number = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for word in file_contents.split():
        word_number += 1
    print(f"Found {word_number} total words")

def main():
    get_book_text()

main()
