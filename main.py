from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    chars = count_characters(book)
    sorted_dictionaries_of_chars_count = sort_dictionary(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dictionaries_of_chars_count:
        print(f"{dictionary['name']}: {dictionary['count']}")
    print("-------------- END -------------------")

main()