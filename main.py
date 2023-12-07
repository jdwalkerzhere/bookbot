def count_words(book_string) -> int:
    return len(book_string.split())


def count_letters(book_string) -> dict:
    letter_dictionary = {}

    for character in book_string.lower():
        if character in letter_dictionary:
            letter_dictionary[character] += 1
        else:
            letter_dictionary[character] = 1

    return letter_dictionary


if __name__ == "__main__":
    book_file_name = "books/frankenstein.txt"
    with open(book_file_name, "r") as book:
        book = book.read()

    word_count = count_words(book)
    print(f"---Beginning Report: {book_file_name}---")
    print(f"{count_words(book)} words found in document\n")
    for char, count in sorted(count_letters(book).items(),
                              key=lambda x: x[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character appears {count} times")
    print("-----------------End Report-----------------")
