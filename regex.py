import re

# Define the regular expression pattern
pattern = re.compile(r'(?:https?://[\w.-]+\.[a-z]+\/[A-Z]\w+|RT\s@\w+|\@\w+|\\n)')

# Open the file for reading
with open("allTweets.txt", "r", encoding="utf8") as file:
    # Read the contents of the file as a single string
    content = file.read()
    # Split the content into an array using a comma as the separator
    array = re.split(r',', content)

    # Create a list to store the results of the regex
    results = [re.sub(pattern, '', value) for value in array]

# Print the list of results
print(results)
