from stats import count_words, character_count, sorted_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    path = book_path
    text = get_book_text(path)

    word_count = count_words(text)
    print(f"Found {word_count} total words")

    char_count = character_count(text)
    sorted_list = sorted_characters(char_count)
    print("----------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

def count_words(text):
    words = text.split()
    return len(words)

main()