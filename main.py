import sys
from stats import count_words
from stats import count_character_occurrences
from stats import sort_character_counts

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    """Reads the book file and prints word and character counts."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_counts = count_character_occurrences(book_text)
    sorted_char_counts = sort_character_counts(char_counts)

    print(f"Found {num_words} total words")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")

if __name__ == "__main__":
    main()