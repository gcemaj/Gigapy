from gigaword_api import Gigaword

def main():
    giga = Gigaword('../Corpus')
    print(giga.corpora)
    print(giga.documents)
    giga.getFile(giga.corpora[0],0)

if __name__ == '__main__': main()