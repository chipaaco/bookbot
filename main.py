import sys
from stats import get_num_words
from stats import get_num_times_each_word
from stats import sorted_list_dict

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    get_num_words(path)
    print("--------- Character Count -------")
    dictionary = get_num_times_each_word(path)
    for dictio in sorted_list_dict(dictionary):
        if dictio["char"].isalpha():
            print(f"{dictio["char"]}: {dictio["num"]}")
        
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
    print(book_path)
    main(book_path)
