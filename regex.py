import re

# Open the file for reading
with open("allTweets.txt", "r", encoding="utf8") as file:
    # Read the contents of the file as a single string
    content = file.read()
    array = content.split(",")

    # Define the regular expression pattern
pattern = re.compile(r'https?://[\w.-]+\.[a-z]+\/[A-Z]\w+|RT\s@\w+|\@\w+|\\n')

# Create a list to store the results of the regex
results = []

for value in array:
    # Apply the regular expression to the value
    match = re.search(pattern, value)
    
    # If a match is found, add it to the results list without the matching text
    if match:
        results.append(value.replace(match.group(0), ""))


# Print the list of results
print(results)