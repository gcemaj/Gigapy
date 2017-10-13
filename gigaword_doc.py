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
        print(self.parseByTagName('HEADLINE'))
        print(self.parseByTagName('DATELINE'))
        print(self.parseByTagName('TEXT'))
        print(self.parseText())

    def parseByTagName(self,name):
        result = ''
        for i in self.doc.iter(name):
            result  += i.text

        return result

    def parseText(self):
        temp = self.parseByTagName('TEXT')
        return self.parseByTagName('P') if temp == 0 else temp


    
