import os.path
import json
import sys
from singleton import  Singleton



@Singleton
class FileManager:

    FOLDER = "docs/"
    INDEX = "docs/index.index"



    def __init__(self):
        try:

            with open(self.INDEX, 'rb') as fp:
                self._dictionary =  json.load(fp)
            print "Dizionario esistente in " + self.INDEX
        except:
            #print "Unexpected error initializing dictionary:", sys.exc_info()[0]
            print "Dizionario inesistente, creato ex novo"
            #self.dictionary = json.dump({'index':0, 'files':{} })
            self._dictionary = { 'sequence': 0 , 'files': [] }



    #il Dizionario va aggiornato solo in caso di nuovo elemento, per gli altri va aggiornato solo il contenuto del file
    def __updateDictionary(self, title):
        print "updateDictionary()"

        lastId = self._dictionary['sequence']
        id = lastId + 1
        self._dictionary['sequence'] = id
        files = self._dictionary['files']
        files.append({ 'id':id, 'title' : title })

        with open(self.INDEX, 'wb') as outfile:
            json.dump(self._dictionary, outfile)
        print "Update dizionario completato"

        return id



    def salvaNuovo(self, title,text):
        id = self.__updateDictionary(title)
        self.__salvaFile(id,text)


    def __salvaFile(self,id,text):
        path = self.FOLDER + str(id) + ".txt"
        out_file = open(path,"w")
        out_file.write(text)
        out_file.close()

    def salvaEsistente(self,id,text):
        self.__salvaFile(id,text)

    def getTextEsistente(self,id):
        path = self.FOLDER + str(id) + ".txt"
        in_file = open(path,"r")
        text =  in_file.read()
        in_file.close()
        return text

    def getDictionary(self):
        return self._dictionary

    def delete(self,id):
        print "delete()" + str(id)
        files = self._dictionary['files']
        #for obj in files:
        #    if (int(obj['id']) == id):
        #        files.pop(obj)
        #        obj.remove()
        #files.append({ 'id':id, 'title' : title })

        for c in files:
            print c.get('id')
            if (str(c.get('id')) == str(id)):
                print "EUREKA"

        print files
        files[:] = [d for d in files if str(d.get('id')) != str(id)]

        print files
        #print "1"
        #print files
        #print "2"
        #print self._dictionary

        with open(self.INDEX, 'wb') as outfile:
            json.dump(self._dictionary, outfile)
        print "delete() finito"

