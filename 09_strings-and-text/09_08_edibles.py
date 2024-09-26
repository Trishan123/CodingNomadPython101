# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# Extracting the food items using string slicing
apple = s[7:12]    # 'apple'
egg = s[26:29]     # 'egg'
butter = s[57:63]  # 'butter'
flour = s[68:73]   # 'flour'

# Print the extracted words
print(apple)   # Output: apple
print(egg)     # Output: egg
print(butter)  # Output: butter
print(flour)   # Output: flour
