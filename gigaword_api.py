'''
This is an API to more easily interact with the gigaword dataset 
'''

import os
import gzip
import xml.etree.ElementTree as etree 
from gigaword_doc import GigaDoc

class Gigaword:

    def __init__(self,path):
        # Path to data
        self.path = path
        self.corpora = self.getCorpora()
        self.documentNames = self.getDocumentNames()
        self.documentsByCorpora = self.loadDocuments()

    def getDocumentNames(self):
        documents = {i:[] for i in self.corpora}
        for i in self.corpora:
            documents[i] += [name for name in os.listdir(os.path.join(self.path,i)) if os.path.isfile(os.path.join(self.path, i ,name))]
        return documents

    def getCorpora(self):
        return [name for name in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, name))]

    
    def loadDocuments(self):
        documents = {}
        for i in self.corpora[:2]:
            documents[i] = self.loadDocumentsByCorpus(i)
        return documents


    def loadDocumentsByCorpus(self,corpus):
        result = []
        for doc in self.documentNames[corpus]:
            with gzip.open(os.path.join(self.path,corpus,doc),'rb') as f:
                xml = '<root>' +  f.read() + '</root>'
            print(xml)
            tree = etree.fromstring(xml)
            # for i in tree.getchildren():  
            #     a = GigaDoc(i)
            #     print(a.id)
            #     result.append(GigaDoc(i))
        return result    


    def getFile(self,corpus,index):
        if index > len(self.documentNames[corpus]) : 
            return None
        else:
            with gzip.open(os.path.join(self.path,corpus,self.documentNames[corpus][index]),'rb') as f:
                xml = '<root>' +  f.read() + '</root>'

            tree = etree.fromstring(xml)
            temp = tree.getchildren()      
            doc = GigaDoc(temp)         