from nlphw1.languagemodel import LanguageModel


def main():
    languageModel: LanguageModel = LanguageModel(n=3)

    positiveReviewDirectoryPath: str = "./../data/Pos"
    negativeReviewDirectoryPath: str = "./../data/Neg"

    languageModel.processDirectory(positiveReviewDirectoryPath)
    languageModel.processDirectory(negativeReviewDirectoryPath)

    topNGramThreshold: int = 10
    # Top 10 N-Gram Analysis
    print("\nTop 10 N-Gram Analysis:")

    # Positive Review Analysis
    # Bi-Gram
    positiveReviewBiGramLangModel: LanguageModel = LanguageModel(2)
    positiveReviewBiGramLangModel.processDirectory(positiveReviewDirectoryPath)
    positiveReviewBiGramLangModel.printTopNGrams("Positive Review Bi-Grams", topNGramThreshold)

    # Tri-Gram
    positiveReviewTriGramLangModel: LanguageModel = LanguageModel(3)
    positiveReviewTriGramLangModel.processDirectory(positiveReviewDirectoryPath)
    positiveReviewTriGramLangModel.printTopNGrams("Positive Review Tri-Grams", topNGramThreshold)

    # Negative Review Analysis
    # Bi-Gram
    negativeReviewBiGramLangModel: LanguageModel = LanguageModel(2)
    negativeReviewBiGramLangModel.processDirectory(negativeReviewDirectoryPath)
    negativeReviewBiGramLangModel.printTopNGrams("Negative Review Bi-Grams", topNGramThreshold)

    # Tri-Gram
    negativeReviewTriGramLangModel: LanguageModel = LanguageModel(3)
    negativeReviewTriGramLangModel.processDirectory(negativeReviewDirectoryPath)
    negativeReviewTriGramLangModel.printTopNGrams("Negative Review Tri-Grams", topNGramThreshold)

    # All Review Analysis
    # Bi-Gram
    allReviewBiGramLangModel: LanguageModel = LanguageModel(2)
    allReviewBiGramLangModel.processDirectory(positiveReviewDirectoryPath)
    allReviewBiGramLangModel.processDirectory(negativeReviewDirectoryPath)
    allReviewBiGramLangModel.printTopNGrams("All Review Bi-Grams", topNGramThreshold)

    # Tri-Gram
    allReviewTriGramLangModel: LanguageModel = LanguageModel(3)
    allReviewTriGramLangModel.processDirectory(positiveReviewDirectoryPath)
    allReviewTriGramLangModel.processDirectory(negativeReviewDirectoryPath)
    allReviewTriGramLangModel.printTopNGrams("All Review Tri-Grams")

    print("\nAll Review Language Model General Information:")
    print("\tTotal Word Tokens:", allReviewTriGramLangModel.getTotalWordTokens())
    print("\tUnique Word Count:", allReviewTriGramLangModel.getVocabularySize())
    print("\tUnique Tri-Gram Count:", allReviewTriGramLangModel.getUniqueNGramsCount())
    print("\tUnique Bi-Gram Count:", allReviewBiGramLangModel.getUniqueNGramsCount())

    t1 = ("i", "went", "to")
    t2 = ("i", "went", "there")
    t3 = ("one", "of", "the")
    t4 = ("the", "coast", "guard")
    t5 = ("a", "lot", "of")

    print("\nProbability Sequence Tests:")
    print("\t (sequence) : probability")
    print("\t", t1, ":", allReviewTriGramLangModel.getNGramProbability(t1))
    print("\t", t2, ":", allReviewTriGramLangModel.getNGramProbability(t2))
    print("\t", t3, ":", allReviewTriGramLangModel.getNGramProbability(t3))
    print("\t", t4, ":", allReviewTriGramLangModel.getNGramProbability(t4))
    print("\t", t5, ":", allReviewTriGramLangModel.getNGramProbability(t5))


if __name__ == '__main__':
    main()
