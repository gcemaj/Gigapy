from gigaword_api import Gigaword

def printToFile(name,sentences):
    with open(name, "w",encoding='utf-8') as file:
        file.writelines( "%s\n" % item for item in sentences )

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    sentences = giga.getSentencesFromKDocs((0.7,0.2,0.1),10)
    printToFile('../trainGigaEnglish.text',sentences[0])
    printToFile('../valGigaEnglish.text',sentences[1])
    printToFile('../testGigaEnglish.text',sentences[2])

if __name__ == '__main__': main()