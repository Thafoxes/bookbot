
def text_to_string(file_contents):
    return file_contents.split()

def main():
    print("starting")
    with open("books/frankenstein.txt") as file:
        file_content = file.read()

        words = text_to_string(file_content)
        print(len(words))


        lowered_string = file_content.lower()
        lowered_string = text_to_string(lowered_string)
        characters_count = {}
        for word in lowered_string:
            word.split()
            for char in word:
                characters_count[char] = characters_count.get(char, 0) + 1

        print(characters_count)

if __name__ == "__main__":
    main()