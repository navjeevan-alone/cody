from difflib import get_close_matches

def find_best_match(input_str, array_of_objects):
    commands = [obj['command'] for obj in array_of_objects]
    matches = get_close_matches(input_str, commands)
    if matches:
        best_match = matches[0]
        index = commands.index(best_match)
        return array_of_objects[index]['function']
    else:
        return None  # No match found

def googleSearch():
    print("Dummy Google search function called.")

def playMusic():
    print("Dummy play music function called.")

def openBrowser():
    print("Dummy open browser function called.")

# Example usage:
commands_and_functions = [
    {"command": "search", "function": "googleSearch()"},
    {"command": "play music", "function": "playMusic()"},
    {"command": "open browser", "function": "openBrowser()"}
]
input_str = "search"
function = find_best_match(input_str, commands_and_functions)
if function is not None:
    print(f"Best match found. Calling function: {function}")
    # Call the function associated with the best match
    eval(function)
else:
    print("No match found.")
