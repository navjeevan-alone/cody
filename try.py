from difflib import get_close_matches

def find_best_match(input_str, array_of_strings):
    matches = get_close_matches(input_str, array_of_strings)
    if matches:
        best_match = matches[0]
        return array_of_strings.index(best_match)
    else:
        return None  # No match found

# Example usage:
array_of_strings = ["apple", "banana", "orange", "pear", "peach"]
input_str = "ora"
index = find_best_match(input_str, array_of_strings)
if index is not None:
    print(f"Best match found at index: {index}")
else:
    print("No match found.")
