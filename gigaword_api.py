'''
This is an API to more easily interact with the gigaword dataset 
'''

import os
import gzip
import xml.etree.ElementTree as etree 
import random
from gigaword_doc import GigaDoc

class Gigaword:

    def __init__(self,path):
        # Path to data
        self.path = path
        self.corpora = self.getCorpora()
        self.documentNames,self.allDocsNum = self.getDocumentNames()

    def getDocumentNames(self):
        documents = {i:(0,[]) for i in self.corpora}
        totalDocuments = 0
        for i in self.corpora:
            tempSize = documents[i][0] 
            tempList = documents[i][1] 
            tempList += [name for name in os.listdir(os.path.join(self.path,i)) if os.path.isfile(os.path.join(self.path, i ,name))]
            tempSize += len(tempList)
            documents[i] = (tempSize,tempList)
            totalDocuments += tempSize
        return documents,totalDocuments

    def getCorpora(self):
        return [name for name in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, name))]

    
    def loadDocuments(self):
        documents = {}
        for i in self.corpora:
            documents[i] = self.loadDocumentsByCorpus(i)
        return documents

    def getSentencesFromKDocs(self,distribution,k):
        
        trainSentences = []
        valSentences = []
        testSentences = []

        percentOfAllDocs = float(k)/float(self.allDocsNum)
        for i in self.corpora:
            corpusSize, corpusNames = self.documentNames[i]
            numFromCorpus = int(corpusSize * percentOfAllDocs)
            randomNames = random.shuffle(corpusNames)
            counter = 0
            index = 0
            while counter < numFromCorpus:
                doc = randomNames[index]
                with gzip.open(os.path.join(self.path,i,doc),'rb') as f:
                    xml = '<root>' +  f.read() + '</root>'
                try:
                    tree = etree.fromstring(xml)
                    counter += 1
                    for i in tree.getchildren():  
                        gigaDoc = GigaDoc(i)
                        sentncesSize = len(gigaDoc.sentences)

                        numberTrain = int(distribution[0]*sentncesSize)
                        numberVal = int(distribution[1]*sentncesSize)
                        numberTest = sentncesSize - numberVal - numberTrain

                        randomSentences = random.shuffle(gigaDoc.sentences)

                        trainSentences += randomSentences[:numberTrain]
                        valSentences += randomSentences[numberTrain:numberTrain+numberVal]
                        testSentences += randomSentences[numberTrain+numberVal:numberTrain+numberVal+numberTest]
                        
                except:
                    print('fuck')
                    index += 1
                    continue

            print(trainSentences,valSentences,testSentences)

        pass

    
    def loadDocumentsByCorpus(self,corpus):
        result = []
        for doc in self.documentNames[corpus]:
            with gzip.open(os.path.join(self.path,corpus,doc),'rb') as f:
                xml = '<root>' +  f.read() + '</root>'
            try:
                tree = etree.fromstring(xml)
                for i in tree.getchildren():  
                    a = GigaDoc(i)
                    result.append(GigaDoc(i))
            except:
                print('fuck')
                continue


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