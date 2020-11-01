import itertools

with open("words.txt", "r") as wordlist_file:
    wordlist = wordlist_file.read()

subject_word = "suvat"
subject_word_chars = list(subject_word)

combos =  list(itertools.permutations(subject_word_chars))
combos = ["".join(word) for word in combos]
print(combos)

for word in combos:
    if word in wordlist:
        print(word)

if "aback" in wordlist:
    print("test")
