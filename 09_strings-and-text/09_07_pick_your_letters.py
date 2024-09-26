# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

# Build the sentence using indexing
message = (
    word[1] + word[2] +          # 'w' + 'e' -> 'we'
    word[8] +                    # ' '       -> 'we '
    word[7] + word[5] + word[2] +# 's' + 'e' + 'e' -> 'see'
    word[8] +                    # ' '       -> 'we see '
    word[0] + word[6] + word[3] + word[5] + word[7] # 't' + 'r' + 'e' + 'e' + 's' -> 'trees'
)

print(message)

