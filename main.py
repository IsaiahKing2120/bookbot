import sys
from stats import num_words, count_characters, sort_on


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)

    word_count = num_words(text)
    char_counts = count_characters(text)

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()

