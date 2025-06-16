import sys
from stats import get_num_words, get_char_count, get_sorted_dicts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path) as file:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        text = get_book_text(file)
        print("----------- Word Count ----------")
        words = get_num_words(text)
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        char_count = get_char_count(text)
        sorted_chars = get_sorted_dicts(char_count)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

def get_book_text(file):
    return file.read()

main()