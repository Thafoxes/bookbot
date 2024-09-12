
def text_to_string(file_contents):
    return file_contents.split()

def convert_words_to_count_characters(lowered_string):
    characters_count = {}
    for word in lowered_string:
        word.split()
        for char in word:
            characters_count[char] = characters_count.get(char, 0) + 1
    return characters_count

def main():
    print("starting")
    with open("books/frankenstein.txt") as file:
        file_content = file.read()

        words = text_to_string(file_content)

        lowered_string = file_content.lower()
        lowered_string = text_to_string(lowered_string)
        characters_count = convert_words_to_count_characters(lowered_string)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document \n")
        for charactrer, count in characters_count.items():
            print(f"The '{charactrer}' was found {count} times")

if __name__ == "__main__":
    main()