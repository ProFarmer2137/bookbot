def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for char in sorted(char_count.keys()):
        print(f"The '{char}' character was found {char_count[char]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
