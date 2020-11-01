import string
import itertools

# Javascript

javascript = """
function try_attack (word) {
    winning_answer.value = word;
    calculateAnswer() 
}
var words = [wordlist];
var winning_answer = document.getElementById("winning-answer");
for (word of words) {
    var my_var = setTimeout(try_attack, 100, word)
}
"""

# Components of word list
low_letters = string.ascii_lowercase
up_letters = string.ascii_uppercase
digits = string.digits

# Combine components to make string wordlist, case sensitive and not
chars = low_letters + digits
inc_chars = low_letters + up_letters + digits

# Test pring
print(chars)
print(inc_chars)

#Length of codes
length = 4
# Make all combinations, cast tuples to strings
words = list(itertools.permutations(chars, length))
print("done 1")
words = [''.join(word) for word in words]
words = str(words)
javascript = javascript.replace("[wordlist]", words)
print("done 2")
##print(words)
with open("attack.txt", "w") as file:
    file.write(javascript)
print("done 3")

# Print with newlines for extensions     
##words = "\n".join(words)
##print(words)







