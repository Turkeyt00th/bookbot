def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def count_character_occurrences(text):
    """Counts the occurrences of each character (case-insensitive) in a string, excluding spaces."""
    char_counts = {}
    for char in text.lower():
        if char != ' ':  # Ignore spaces
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_character_counts(char_counts):
    """Takes a dictionary of character counts and returns a sorted list of dictionaries."""
    sorted_counts_list = []
    for char, count in char_counts.items():
        sorted_counts_list.append({'char': char, 'count': count})

    def sort_by_count(item):
        return item['count']
    
    sorted_counts_list.sort(key=sort_by_count, reverse=True)
    return sorted_counts_list