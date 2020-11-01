import random
import itertools
import pyttsx3

# Sentence to be mixed, in list form
##meem = ["me", "and", "the", "boys", "at", "2am", "looking", "for", "BEANS"]
##meem = ["oh heck", "oh frick", "he's got airpods in", "he can't hear us"]
##meem = ["understandable", "have", "a", "nice", "day"]
meem = ["what's", "gibby", "thinking", "about"]
##meem = ["hello", "hi"]


print("Permutating")

# Create list of permutations
perms = list(itertools.permutations(meem))
# Shuffle for more variety
random.shuffle(perms)
# Convert each permutation list to string
perms = list(map(lambda x: " ".join(x), perms))

# This section merges arbitrary numbers of lists to make reading smoother
new = []
# Increment for list merging
inc = 1000
# Iterate and merge
for i in range(0, len(perms), inc):
    new.append(" ".join(perms[i:i+inc]))
##    print(" ".join(perms[i:i+inc]))
perms = new
del new

print("Done")

def BEANS(name, location, length):
    print(length, end="")
    print(engine.getProperty('voice'))
    if length == 5:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

# Initialise tts engine
engine = pyttsx3.init()
# Link the word event listener
##engine.connect('started-word', BEANS)

# Set speech rate
rate = engine.getProperty('rate')
# Default rate is 200.
rate = 100
engine.setProperty('rate', rate)
print("Rate " + str(rate))


# Print and say each bit
for line in perms:
    print(line)
    engine.say(line)
    engine.runAndWait()



