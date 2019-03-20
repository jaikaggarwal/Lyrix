import re
import time

class LyricMasker:
    def __init__(self, lyrics):
        self.processed_lyrics = self.preprocess(lyrics)
        self.mapping = {}
        self.create_mapping()
        print(self.mapping)

    def preprocess(self, lyrics):
        """
        Gets rid of new line characters as well as unnecessary punctuation.
        :param lyrics: string of lyrics text
        :return: list[string] split up list of preprocessed lyrics
        """
        lyrics = re.sub(r"[,()]", '', lyrics)
        lyrics = re.sub(r"(\n+)", " ", lyrics)
        return lyrics.split(" ")

    def create_mapping(self):
        """
        Creates a dictionary where keys are the words (strings) and values
        are list of indices the word appears at (list[int]). To be used when Angular added.
        """
        for i in range(len(self.processed_lyrics)):
            word = self.processed_lyrics[i].lower()
            if word not in self.mapping:
                self.mapping[word] = [i]
            else:
                self.mapping[word].append(i)

    def get_mapping(self):
        return self.mapping

    def get_processed_lyrics(self):
        return self.processed_lyrics

    def display(self):
        for word in self.processed_lyrics:
            if word in self.mapping:
                print("_____")
            else:
                print(word)

    def check(self, word):
        #Todo: make sure capitalization doesn't matter
        if word in self.mapping:
            print("Good job!")
            self.mapping.pop(word)
        else:
            print("Try again!")
        time.sleep(0.5)


    def game(self):
        while len(self.mapping.keys()) > 0:
            self.display()
            self.check(input("Make a guess: "))