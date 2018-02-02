import os
from typing import Dict, List, Tuple
import pprint

from nlphw1.utility import cleanText


# Represents the Language Model for currently processed database
class LanguageModel(object):
    def __init__(self, n: int):
        # N-Gram to N-Gram Frequency mapping
        self._nGramFrequency: Dict[Tuple, int] = {}
        # N-Gram size
        self._n: int = n
        # List of unique words in database
        self._vocabulary: List[str] = []
        # Total word tokens processed
        self._totalWordTokens: int = 0

    def getVocabulary(self) -> List[str]:
        return self._vocabulary

    def getVocabularySize(self) -> int:
        return len(self._vocabulary)

    def getTotalWordTokens(self) -> int:
        return self._totalWordTokens

    def getUniqueNGramsCount(self) -> int:
        return len(self._nGramFrequency.keys())

    # Add a text file to the language models
    def processFile(self, filePath) -> None:
        # Read and clean the file contents
        with open(filePath, 'r') as content_file:
            text: str = content_file.read()
        # Clean the text
        text = cleanText(text)
        # Split the text into words
        words: List[str] = text.split()
        # Add new words to vocabulary
        for word in words:
            self._totalWordTokens += 1
            if word not in self._vocabulary:
                self._vocabulary.append(word)

        for index in range(len(words) - self._n):
            nGram: Tuple = tuple(words[index:index + self._n])
            self.incrementNGramFrequency(nGram)

    # Add all text files contained within a given directory
    def processDirectory(self, directory) -> None:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filePath = os.path.join(directory, filename)
                self.processFile(filePath)

    # Increment the Frequency of a given nGram
    def incrementNGramFrequency(self, nGram: Tuple, deltaFrequency: float=1) -> None:
        currentNGramFrequencyValue = self._nGramFrequency.get(nGram, 0)
        currentNGramFrequencyValue += deltaFrequency
        self._nGramFrequency[nGram] = currentNGramFrequencyValue

    # Get the probability of the last word appearing in a given N-Gram P(wN | w1, w2, ..., wN-1)
    def getNGramProbability(self, nGram: Tuple) -> float:
        if len(nGram) != self._n:
            raise Exception("The given N-Gram", nGram, "has a length of", len(nGram),
                            "but this language model has a required nGram length of", self._n,
                            "please provide an N-Gram with length of", self._n)

        # (w1, w2, ..., wN-1)
        previousWords = nGram[:-1]

        # The N-Grams the match the given N-Gram for every word expect wN
        partiallyMatchedNGrams = [
            item for item in self._nGramFrequency.items()
            if item[0][:self._n - 1] == previousWords
        ]

        # The total frequency of all partially matched N-Grams
        partiallyMatchedNGramsFrequency = sum([
            partiallyMatchedNGram[1] for partiallyMatchedNGram in partiallyMatchedNGrams
        ])

        # The frequency of the given N-Gram
        exactMatchFrequency: int = self._nGramFrequency.get(nGram, 0)
        v: int = self.getVocabularySize()
        return (exactMatchFrequency + 1) / (partiallyMatchedNGramsFrequency + v)

    def getTopNGrams(self, topNGramThreshold: int = 10, sortInAscendingOrder: bool = True):
        items = sorted(self._nGramFrequency.items(), key=lambda x: x[1])
        if sortInAscendingOrder:
            items.reverse()
        return items[:topNGramThreshold]

    def printTopNGrams(self, title: str = "", topNGramThreshold: int = 10, sortInAscendingOrder: bool = True) -> None:
        topNGrams = self.getTopNGrams(topNGramThreshold, sortInAscendingOrder)
        print("Top", topNGramThreshold, ":", title)
        pp = pprint.PrettyPrinter(indent=4, width=150)
        pp.pprint(topNGrams)
