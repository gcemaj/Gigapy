from gigaword_api import Gigaword

def main():
    giga = Gigaword('/home/rldata/gigaword/data')
    giga.getFile(giga.corpora[0],0)

if __name__ == '__main__': main()