def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Returns a dictionary with the count of each alphabetical character in the text."""
    text = text.lower()  # Convert text to lowercase
    char_count = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def sort_on(dict):
    """Sorting function to get the value of 'num' key."""
    return dict["num"]

def print_report(word_count, char_count, file_path):
    """Prints a formatted report of word and character counts."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert dictionary to list of dictionaries for sorting
    sorted_characters = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_characters.sort(reverse=True, key=sort_on)

    for entry in sorted_characters:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

    print(f"--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)  # Count words
    char_count = count_characters(file_contents)  # Count characters

    print_report(word_count, char_count, path_to_file)

if __name__ == "__main__":
    main()
