import sys

from stats import get_book_text, get_num_words, count_characters, transform_dict_to_sorted_list, sort_on  # import the functions from the stats.py file

def main(args):
    """
    Main function that orchestrates the book reading process.
    
    This function:
    1. Calls get_book_text() to read the book
    2. Calls get_num_words() to count the number of words in the book
    3. Calls count_characters() to count the number of characters in the book
    4. Calls transform_dict_to_sorted_list() to sort the characters by count
    5. Prints the results to the console
    """

    # Get the text content of the book and count the number of words and characters
    book_text = get_book_text(args[0])
    num_words_in_book = get_num_words(book_text)
    characters_in_book = count_characters(book_text)
    characters_in_book_sorted = transform_dict_to_sorted_list(characters_in_book)
    
    # Print the entire book text to the console         
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[0]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")
    print("--------- Character Count -------")
    #Prints the characters in the book and their counts, excluding non-alphabetic characters
    for character, count in characters_in_book_sorted:
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


# Execute the main function when the script is run directly
if __name__ == "__main__":

    # Checks if the user has provided a book name
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1:])