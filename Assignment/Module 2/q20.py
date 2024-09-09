# Write a Python function that takes a list of words and returns the length of the longest one.
def len_longest_word(words):
    max_words=0
    for w in words:
        if len(w) > max_words:
            max_words = len(w)
    return max_words
words=['python','java','kotlin','javascript','mysql']
print(len_longest_word(words))