def get_book_text(book_name):
    """
    Reads and returns the text content of a book file.
    
    Args:
        book_name (str): The name and path of the book file (with .txt extension)
    
    Returns:
        str: The complete text content of the book file
    
    Note:
        The function expects the book file to be in the same directory as the script.
        It uses UTF-8 encoding to handle special characters.
    """
    # Open the book file from the books directory with UTF-8 encoding
    # The 'with' statement ensures the file is properly closed after reading
    with open(f"{book_name}", "r", encoding="utf-8") as file:   
        return file.read()

def get_num_words(book_text):
    """
    Counts the number of words in the book text.
    
    Args:
        book_text (str): The text content of the book
    
    Returns:
        int: The number of words in the book
    """
    return len(book_text.split())

def count_characters(book_text):
    """
    Counts the number of characters in the book text.
    
    Args:
        book_text (str): The text content of the book
    
    Returns:
        dict: A dictionary with characters as keys and their counts as values
    """
    characters_lower_case = book_text.lower()

    #Counts characters in the book and saves them in a dictionary
    characters_count = {}
    for char in characters_lower_case:
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
            
    return characters_count

def transform_dict_to_sorted_list(characters_count):
    """
    Transforms the dictionary into a list of tuples and sorts them by value in descending order.
    """
    return sorted(characters_count.items(), key=sort_on, reverse=True)

def sort_on(item):
    """
    Sorts the dictionary by value in descending order
    """
    return item[1]
