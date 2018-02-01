import re
import string


def cleanText(text: str) -> str:
    cleanedText = text
    # Remove line endings
    cleanedText = cleanedText.replace("\r", "").replace("\n", " ")
    # To lowercase
    cleanedText = cleanedText.lower()
    # Remove Punctuation
    cleanedText = removePunctuation(cleanedText)
    return cleanedText


def removePunctuation(text: str) -> str:
    return re.sub("[" + string.punctuation + "]", "", text)
