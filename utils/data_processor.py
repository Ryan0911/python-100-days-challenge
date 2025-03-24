"""Description: Load data from files."""
def load_word_list(filename="data/words.txt"):
    """Load a list of words from a file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        list: A list of words from the file.
    """
    with open(filename, "r", encoding= "utf-8") as file:
        words = [line.strip() for line in file if len(line.strip()) > 3]
    return words
