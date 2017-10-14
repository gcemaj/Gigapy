from gigaword_api import Gigaword
import codecs

def printToFile(name,sentences):
    with codecs.open(name, "w",encoding='utf-8') as file:
        file.writelines( "%s\n" % item for item in sentences )

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    sentences = giga.getSentencesFromKDocs((0.7,0.2,0.1),10)
    print("done processing")
    printToFile('../data/trainGigaEnglish.txt',sentences[0])
    printToFile('../data/valGigaEnglish.txt',sentences[1])
    printToFile('../data/testGigaEnglish.txt',sentences[2])

if __name__ == '__main__': main()