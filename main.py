from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_by_frequency(item):
    return item[1]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    char_list = [(char, count) for char, count in chars_dict.items() if char.isalpha()]
    char_list.sort(key=sort_by_frequency, reverse=True)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char, count in char_list:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()