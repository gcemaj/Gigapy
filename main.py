from gigaword_api import Gigaword

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    giga.getKSentences((0.7,0.2,0.1),200)
    # for i in giga.corpora:
    #     print("POOP",giga.documentsByCorpora[i][0].sentences)

if __name__ == '__main__': main()