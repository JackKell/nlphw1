import os
import pprint
from typing import Dict, List, Tuple

from nlphw1.utility import cleanText


class LanguageModel(object):
    def __init__(self, n: int):
        self._nGramFrequency: Dict[Tuple, int] = {}
        self._n: int = n
        self._vocabulary: List[str] = []
        self._totalTokens: int = 0

    def getVocabulary(self) -> List[str]:
        return self._vocabulary

    def getVocabularySize(self) -> int:
        return len(self._vocabulary)

    def getTotalTokens(self) -> int:
        return self._totalTokens

    def getTotalUniqueNGrams(self) -> int:
        return len(self._nGramFrequency.keys())

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
            self._totalTokens += 1
            if word not in self._vocabulary:
                self._vocabulary.append(word)

        for index in range(len(words) - self._n):
            nGram: Tuple = tuple(words[index:index + self._n])
            self.incrementNGramFrequency(nGram)

    def processDirectory(self, directory) -> None:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filePath = os.path.join(directory, filename)
                self.processFile(filePath)

    def incrementNGramFrequency(self, nGram: Tuple, value=1) -> None:
        currentNGramFrequencyValue = self._nGramFrequency.get(nGram, 0)
        currentNGramFrequencyValue += value
        self._nGramFrequency[nGram] = currentNGramFrequencyValue

    def getNGramProbability(self, previousWords: Tuple[str, ...], lastWord: str):
        nGram: Tuple = tuple(list(previousWords) + [lastWord])
        print(nGram)
        # If the previous words less than 1 - the size of the nGram
        if len(previousWords) != self._n - 1:
            return False

        matchedNGrams = [
            item for item in self._nGramFrequency.items()
            if item[0][:self._n - 1] == previousWords
        ]

        matchedNGramsFrequency = sum([
            matchedNGram[1] for matchedNGram in matchedNGrams
        ])

        exactMatchFrequency: int = self._nGramFrequency.get(nGram, 0)

        print(matchedNGrams)
        print("Matched N-Grams Frequency:", matchedNGramsFrequency)
        print("Exact Match Frequency:", exactMatchFrequency)
        # v: int = len(self._vocabulary)
        v: int = len(self._nGramFrequency)
        print(exactMatchFrequency + 1)
        print(matchedNGramsFrequency + v)
        return (exactMatchFrequency + 1) / (matchedNGramsFrequency + v)

    def getTopNGrams(self, top: int = 10, sortInAscendingOrder: bool = True):
        items = sorted(self._nGramFrequency.items(), key=lambda x: x[1])
        if sortInAscendingOrder:
            items.reverse()
        return items[:top]

    def printStats(self):
        pp = pprint.PrettyPrinter(indent=4, width=150)
        pp.pprint(len(self._vocabulary))
        pp.pprint(len(self._nGramFrequency))
        print("Total Unique Tokens", self._totalTokens)
        pp.pprint(self._nGramFrequency)
        pp.pprint(self.getTopNGrams())
