def get_num_words():
    word_number = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    for word in file_contents.split():
        word_number += 1
    print(f"Found {word_number} total words")

def get_num_times_each_word():
    raw_chars = []
    dictionary = {}

    # lista con caracteres
    # limpiado tambien de saltos y caracteres especiales asdfasdf
    with open("books/frankenstein.txt") as f:
        for digit in f.read():
            if digit != '\ufeff' and digit != "\n":
                raw_chars.append(digit.lower())
    # print(raw_chars)

    # llenar diccionario
    # sumar 1 segun cada keyvalue posicionado: word count
    for char in raw_chars:
        if char in dictionary:
            dictionary[char] = dictionary[char]+1
            # print(f"existe keyvalue: {char} wc: {dictionary[char]}")
        else:
            dictionary[char] = 1
            # print(f"se crea keyvalue: {char} wc: {dictionary[char]}")

    # imprimir la wea
    return dictionary
