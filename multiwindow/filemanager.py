import os.path
import json
import sys


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            #Al primo richiamo e' corretto che non sia presente l'istanza
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


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
        files.append({ id : title })

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


    def __generaNome(self,id,title):

        if (id == 0):
            # Legge un file.
            in_file = open(self.INDEX,"r")
            nextId = int(in_file.read()) + 1
            in_file.close()
            out_file = open(self.INDEX,"w")
            out_file.write(str(nextId))
            id = nextId

        substringTitle = title[:20]
        return "" + str(id) + "- " + substringTitle + ".txt"

    def save(self,id, title, text):

        nomeFile = self.__generaNome(id,title)
        out_file = open(self.FOLDER + nomeFile,"w")
        out_file.write(text)
        out_file.close()



