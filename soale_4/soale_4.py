import string
from collections import Counter

# stop words
STOP_WORDS = set(['this', 'is', 'a', 'to','me','should','other','some','i'])

def read_file(file_path):
    """Read the content of a file and return it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("The file is empty.")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError as s:
        print(s)
        return None

def clean_text(text):
    """Remove punctuation and convert text to lowercase."""
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower()

def count_word_frequency(text):
    """Count the frequency of each word in the text, ignoring stop words."""
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    return Counter(filtered_words)

def display_top_words(word_counts, top_n=10):
    """Display the top N most frequent words."""
    most_common = word_counts.most_common(top_n)
    print(f"Top {top_n} most frequent words:")
    for word, count in most_common:
        print(f"{word}: {count}")

def main(file_path):
    """Main function to execute the word frequency analysis."""
    text = read_file(file_path)
    if text:
        cleaned_text = clean_text(text)
        word_counts = count_word_frequency(cleaned_text)
        display_top_words(word_counts)

# Example usage
if __name__ == "__main__":
    main("sample.txt")
