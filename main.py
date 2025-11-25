from stats import get_num_words
from stats import get_num_times_each_word
from stats import sorted_list_dict

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    dictionary = get_num_times_each_word()
    for dictio in sorted_list_dict(dictionary):
        if dictio["char"].isalpha():
            print(f"{dictio["char"]}: {dictio["num"]}")
        

main()
