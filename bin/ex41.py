# random module has various implementations of pseudo-random number
# generators
import random
# urllib.request can import stuff from URLs
# it is similar to the builtin open() function but accepts URLs instead
# of filenames
from urllib.request import urlopen
import sys

# the URL where the words.txt file is saved
# this file has a list of random words
WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

# a dictionary that contains the classes, instances, and dot operators
# as keys and their English language explanation as values
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object): \n\tdef __init__(self, ***):":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object): \n\tdef ***(self, @@@):":
        "class %%% has-a function that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function,  call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first

# testing argument variable (argv[0] is always the name of the script)
# this condition checks whether to make PHRASE_FIRST True or False
# If the first phrase is True then the program displays a message in
# English and the user types in the code and the program tells whether
# the user has typed in the correct code. If the first phase is False
# then the program display the code and the user has to type in english
# what the code means and the program returns the correct answer.
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website. Each line has a single word.
for word in urlopen(WORD_URL).readlines():
    # strip() removes \n from the end of line
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrases):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
