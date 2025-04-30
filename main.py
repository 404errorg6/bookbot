import sys
from stats import word_count
from stats import char_count
from stats import sort
def get_book_text(path):
    with open(path) as f:
        string = f.read()
    return string


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    count = char_count(text)
    print("--------- Character Count -------")
    srt = sort(count)
    for dic in srt:
        char = dic["char"]
        if char.isalpha():
            print(f"{dic["char"]}: {dic["count"]}")

main()