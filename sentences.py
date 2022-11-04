import modes


phrases = """
the brown frog
her small bag
its big plane
their quick zebra
my jynxed video
"""

# Contains all the letters
letters = set("abcdefghijklmnopqrstuvwxyz")
assert len(''.join(sorted(letters - set(phrases)))) == 0

articles = []
adjectives = []
nouns = []

for phrase in phrases.split('\n'):
    if phrase:
        words = phrase.split(' ')
        articles.append(words[0])
        adjectives.append(words[1])
        nouns.append(words[2])


def print_word_bank():
    print("Available Words")
    print("----------------")
    print('Articles:', articles)
    print('Adjectives:', adjectives)
    print('Nouns:', nouns)


def example_sentences():
    sentence_mode = modes.SentenceMode()
    print("Example Sentences")
    print("------------------")
    print(sentence_mode.generate_sample())
    print(sentence_mode.generate_sample())
    print(sentence_mode.generate_sample())
    print(sentence_mode.generate_sample())
    print(sentence_mode.generate_sample())
    print(sentence_mode.generate_sample())

