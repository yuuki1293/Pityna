import patternItem


class Dictionary(object):
    def __init__(self):
        self.random = self.makeRandomList()
        self.pattern = self.makePatternDictionary()

    def makeRandomList(self):
        rfile = open('dics/random.txt', 'r', encoding='utf_8')
        r_lines = rfile.readlines()
        rfile.close()

        randomList = []
        for line in r_lines:
            str = line.rstrip('\n')
            if(str != ''):
                randomList.append(str)
        return randomList

    def makePatternDictionary(self):
        pfile = open('dics/pattern.txt', 'r', encoding='utf_8')
        p_lines = pfile.readlines()
        pfile.close()
        new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if (str != ''):
                new_lines.append(str)

        patternItemList = []
        for line in new_lines:
            ptn, prs = line.split('\t')
            patternItemList.append(patternItem.PatternItem(ptn, prs))
        return patternItemList
    
    def study(self, input):
        input = input.rstrip('\r')
        if not input in self.random:
            self.random.append(input)

    def save(self):
        for index, element in enumerate(self.random):
            self.random[index] = element + '\n'
        with open('dics/random.txt', 'w', encoding='utf_8') as f:
            f.writelines(self.random)