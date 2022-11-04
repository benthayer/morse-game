import random

import helpers
import sentences

class SentenceMode:
    def __str__(self):
        return "Sentence Mode"

    def generate_sample(self):
        article = random.choice(sentences.articles)
        adjective = random.choice(sentences.adjectives)
        noun = random.choice(sentences.nouns)
        sentence = ' '.join([article, adjective, noun])
        return sentence


    def score_sample(self, guess, answer):
        words1 = guess.split(' ')
        words2 = answer.split(' ')

        score = 0
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                score += 1

        print(f"Score: {score}/3")
        return score / 3


class WordMode:
    def score_sample(self, guess, answer):
        if guess == answer:
            print(f"Correct!")
            return 1
        else:
            print("Incorrect")
            return 0


class ArticleMode(WordMode):
    def __str__(self):
        return "Article Mode"

    def generate_sample(self):
        return random.choice(sentences.articles)


class AdjectiveMode(WordMode):
    def __str__(self):
        return "Adjective Mode"

    def generate_sample(self):
        return random.choice(sentences.adjectives)


class NounMode(WordMode):
    def __str__(self):
        return "Noun Mode"

    def generate_sample(self):
        return random.choice(sentences.nouns)

