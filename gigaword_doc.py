import nltk.data
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

sentenceTkzr = nltk.data.load('tokenizers/punkt/english.pickle')

class GigaDoc:

    def __init__(self,doc):
        self.headline = ''
        self.dateline = ''
        self.text = ''
        self.sentences = []
        self.id = ''
        self.doc = doc
        self.parse()

    def parse(self):
        self.id = self.doc.attrib['id'] if 'id' in  self.doc.attrib else ''
        self.headline = self.parseByTagName('HEADLINE')
        self.dateline = self.parseByTagName('DATELINE')
        self.text = self.parseText()
        self.sentences = self.parseSentences()

    def parseByTagName(self,name):
        result = ''
        for i in self.doc.iter(name):
            if len(i.text) >= 4 and len(i.text) < 200:
                result  += i.text
            else:
                print(i.text)

        result = result.replace('\n',' ')
        result = result.replace('\r','')
        result = result.strip()
        return result

    def parseText(self):
        temp = self.parseByTagName('TEXT')
        return self.parseByTagName('P') if temp == '' else temp

    def parseSentences(self):
        return sentenceTkzr.tokenize(self.text)



    
