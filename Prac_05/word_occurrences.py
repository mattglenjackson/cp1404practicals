"""
Word occurrences
Estimated: 20 mins
Actual: 27 mins
"""
# text = "this is a collection of words of nice words this is a fun thing it is"
text = input("Text: ")

word_to_count = {}
words = text.split()
words.sort()

for word in words:
    # frequency = words.count(word)
    # word_to_count[word] = frequency
    frequency = word_to_count.get(word, 0)  # is someone able to explain the difference between these lines and the lines above I commented out?
    word_to_count[word] = frequency + 1

# max_width = max([len(word) for word in words])
max_width = max((len(word) for word in words))  # changed to generator expression as per solutions

for word in word_to_count:
    print(f"{word:{max_width}} : {word_to_count[word]}")
