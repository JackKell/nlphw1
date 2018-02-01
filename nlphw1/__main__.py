from nlphw1.languagemodel import LanguageModel


def main():
    directory: str = "./../data/Pos"
    languageModel: LanguageModel = LanguageModel(n=3)
    # languageModel.processDirectory("./../testdata")
    languageModel.processDirectory("./../data/Pos")
    languageModel.processDirectory("./../data/Neg")
    languageModel.printStats()
    print(languageModel.getNGramProbability(("i", "went"), "to"))
    print(languageModel.getNGramProbability(("i", "went"), "there"))
    print(languageModel.getNGramProbability(("one", "of"), "the"))


if __name__ == '__main__':
    main()
