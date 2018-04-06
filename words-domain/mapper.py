from nltk.corpus import wordnet

class DomainWordMapper:

    def __init__(self, filepath):
        self._domains = {}
        self._synsets = {}
        self._filePath = filepath

    def addOffset(self,synoff):
        return str(synoff).zfill(8)

    def readWNDomain(self, file):
        f = open(file, "r")
        for line in f:
            line = line.rstrip()
            data = line.split("\t")
            offset = str(data[0])
            domain = data[1]
            self._domains[offset] = domain
        f.close()

    def getAllSynsets(self):
        synsets = list(wordnet.all_synsets())
        for synset in synsets:
            key = str(synset.name())
            value = str(self.addOffset(synset.offset()) + "-" + synset.pos())
            self._synsets[key] = value

    def numOfDomains(self, data):
        allDomains = {}
        for key, domain in data.items():
            if domain in allDomains:
                allDomains[domain] = allDomains[domain] + 1
            else:
                allDomains[domain] = 1
        return allDomains

    def writeDataToFile(self, fName, data):
        f = open(fName, "w")
        for key, value in data.items():
            sb = ""
            sb += key + "\t" + str(value)+"\n"
            f.write(sb)
        f.close()

    def getAllWNDomains(self):
        

    def getDomains(self):
        self.readWNDomain(self._filePath['_wndomain'])
        self.getAllSynsets()
        mappingDomains = {}

        #We need take it from db and store it back to db
        if self._filePath['words'] and self._filePath['wordsdomain']:
            words = open(self._filePath['words'], "r")
            wordsdomain = open(self._filePath['wordsdomain'], "w")

        for synset in words:
            syn = wordnet.synsets(synset.strip())[0]
            sb = ""
            if str(syn.name()) in self._synsets:
                offset = self._synsets[str(syn.name())]
                domain = self._domains.get(offset)
                if domain is not None:
                    sb += domain + "\n"
                    mappingDomains[synset] = domain
            else:
                sb += synset + "\t" + "domain_unknown\n"
                mappingDomains[synset] = "domain_unknown"
            if wordsdomain:
                wordsdomain.write(sb)

        numDomain = self.numOfDomains(mappingDomains)
        if self._filePath['domainfreq']:
            self.writeDataToFile(self._filePath['domainfreq'], numDomain)

        if self._filePath['words'] and self._filePath['wordsdomain']:
            words.close()
            wordsdomain.close()

        return numDomain


    def getDomainFromPara(self, words_list):
        self.getAllSynsets()
        mappingDomains = {}

        if self._filePath['words'] and self._filePath['wordsdomain']:
            words = open(self._filePath['words'], "r")
            wordsdomain = open(self._filePath['wordsdomain'], "w")

        if words_list:
            print (words_list)
            for i in range(len(words_list)):
                syn = wordnet.synsets(words_list[i])
                if syn:
                    sb = ""
                    if str(syn[0].name()) in self._synsets:
                        offset = self._synsets[str(syn[0].name())]
                        domain = self._domains.get(offset)
                        if domain is not None:
                            sb += domain + "\n"
                            mappingDomains[synset] = domain
                    else:
                        sb += synset + "\t" + "domain_unknown\n"
                        mappingDomains[synset] = "domain_unknown"
                    if wordsdomain:
                        wordsdomain.write(sb)

            numDomain = self.numOfDomains(mappingDomains)
            if self._filePath['domainfreq']:
                self.writeDataToFile(self._filePath['domainfreq'], numDomain)

            if self._filePath['words'] and self._filePath['wordsdomain']:
                words.close()
                wordsdomain.close()

            return numDomain
