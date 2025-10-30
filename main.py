from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()

    return file_contents


def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath=filepath)
    num_words = get_num_words(book_text)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------

    """)

    for el in get_sorted_char_counts(get_char_counts(book_text)):
        if el['char'].isalpha():
            print(f"{el['char']}: {el['num']}")

main()
