def main():
    book_path = "books/frankenstein.txt"
    print(f"----------Begin report of {book_path}----------")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(text)
    print_report(char_count)
    print("----------------- End report ------------------")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["count"]

def print_report(char_count):
    char_list = []
    for key, value in (char_count.items()):
        if key.isalpha():
            char_list.append({"char": key, "count": value})
    char_list.sort(reverse=True, key=sort_on)
    for x in char_list:
        print("The character {0} was found {1} times".format(x["char"], x["count"]))

main()