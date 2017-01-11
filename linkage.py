import operator
import enchant
import json

class Bigram:
    def __init__(self):
        with open("charBigram.json", mode='r') as json_file:
            self.prob = json.load(json_file)
            print self.prob

    def lookup(self, firstchar, secondchar):
        if self.prob.has_key((firstchar, secondchar)):
            print firstchar,":",secondchar,":", self.prob[(firstchar, secondchar)]
            return self.prob[(firstchar, secondchar)]
        else:
            return 0


class OcrProb:
    def __init__(self):
        self.prob = {
            1: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1700, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            2: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26),
            3: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
                #a  b  c   d   e  f  g  h  i   j   k   l   m   n   o   p   q   r   s   t   u   v  w    x  y   z
        }

    def lookup(self, cur_char_pos, alphabet):
        return self.prob[cur_char_pos][alphabet]



class Tree:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.weight = 0
        self.child = []
        self.found = False

    def setChild(self, node):
        self.child.append(node)

    def getHighProbSuggestedDictWord(self, d, inputWord, biagram):
        highest_prob = -99999
        final_word = ""
        list_of_suggested_words = d.suggest(inputWord)
        for word in list_of_suggested_words:
            prob = 0
            for i in range(len(word)):
                if (i == 0):
                    prob = prob + biagram.lookup("<w>", word[i])
                else:
                    prob = prob + biagram.lookup(word[i - 1], word[i])

            #print prob
            if (prob > highest_prob):
                highest_prob = prob
                final_word = word

        return final_word

    def getHighProbDictWord(self, d, result, firstHighProbWord, found ):
        if (self.alphabet != "<w>"):
            result.append(self.alphabet)

        if len(self.child) != 0:
            for i in range(len(self.child)):
                self.child[i].getHighProbDictWord(d, result, firstHighProbWord, found)
                if (found[0] == True):
                    return

            if (len(result) != 0):
                result.pop()
        else:
            print result
            if (len(firstHighProbWord) == 0):
                firstHighProbWord.append(str(''.join(result)))

            if (d.check(''.join(result)) == True):
                found[0] = True
                return
            result.pop()

    def predictWord(self,bigram):
        d = enchant.Dict("en_US")
        firstHighProbWord = []
        result = []
        found = [False]
        self.getHighProbDictWord(d, result, firstHighProbWord, found)
        if (found[0] == True):
            print ''.join(result)
        else:
            print self.getHighProbSuggestedDictWord(d, firstHighProbWord[0], bigram)

    def buildTree(self, bigram, ocrprob, strlen, depth):
        if (depth == strlen + 1):
            return

        list_of_chars_with_prob = {}
        for c in range(ord('a'), ord('z') + 1):
            list_of_chars_with_prob[chr(c)] = combinedProb(bigram.lookup(self.alphabet, chr(c)),
                                                           ocrprob.lookup(depth, c - 97))

        sorted_list_of_chars_with_prob = sorted(list_of_chars_with_prob.items(), key=operator.itemgetter(1), reverse=1)
        for x in sorted_list_of_chars_with_prob:
            node = Tree(x[0])
            self.setChild(node)
            node.buildTree(bigram, ocrprob, strlen, depth + 1)

    def display(self):
        print "alphabet =", self.alphabet, "weight =", self.weight
        for i in range(len(self.child)):
            self.child[i].display()





def combinedProb(bigramprob, ocrprob):
    return (bigramprob + ocrprob)



bigram = Bigram()
ocrprob = OcrProb()

tree = Tree("<w>")
tree.buildTree(bigram, ocrprob, 3, depth=1)

tree.predictWord(bigram)
# node1.predictWord(result=[])
# # node1.display()
