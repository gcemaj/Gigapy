from gigaword_api import Gigaword

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    # for i in giga.corpora:
    #     print("POOP",giga.documentsByCorpora[i][0].sentences)

if __name__ == '__main__': main()