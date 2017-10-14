from gigaword_api import Gigaword

def printToFile(name,sentences):
    f=open('name,'w')
    for s in sentences:
        f.write(s+'\n')
    f.close()

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    sentences = giga.getSentencesFromKDocs((0.7,0.2,0.1),200)
    printToFile('./trainGigaEnglish.text',sentences[0])
    printToFile('./valGigaEnglish.text',sentences[1])
    printToFile('./testGigaEnglish.text',sentences[2])

if __name__ == '__main__': main()