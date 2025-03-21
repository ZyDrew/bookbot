from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    #Header
    print(12*"=" + " BOOKBOT " + 12*"=")
    print("Analyzing book found at books/frankenstein.txt...")

    # Compte le nombre de mots dans un livre
    print(11*"-" + " Word Count " + 11*"-")
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")

    # Compte le nombre de caractères différents dans un livre (symboles et espaces compris)
    print(9*"-" + " Character Count " + 8*"-")
    char_cout_dict = count_chars(book_text)
    sorted_list = dict_to_sorted_list(char_cout_dict)
    for item in sorted_list:
        print(f"{item["char"]}: {item["count"]}")
    
    print(13*"=" + " END " + 13*"=")

main()