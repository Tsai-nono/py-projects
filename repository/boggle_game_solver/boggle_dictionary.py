# FILE = 'dictionary.txt'
LETTER = 'abcdefghijklmnopqrstuvwxyz'


class Dictionary_Set:

    def __init__(self, diction_file):
        self.diction_file = diction_file
        self.diction_set = set()

    def diction_s(self):

        with open(self.diction_file, 'r') as f:
            for line in f:
                word = line.strip()
                if len(word) >= 4:
                    self.diction_set.add(word)

    def lookup_set_diction(self,word):
        if word in self.diction_set:
            print(f'{word} , have in')
            return True
        return False


class Dictionary_Dict:
    def __init__(self, diction_file):
        self.diction_file = diction_file
        self.dict_map = []
        self.letter_dict = {}

    def diction_dict(self):

        cont = 0
        for i in LETTER:
            d = {}
            d[i] = {}
            self.dict_map.append(d)

            self.letter_dict[i] = cont
            cont += 1

        with open(self.diction_file,'r')	as f:
            for line in f:
                input_word = line.strip()

                # 預設匯入條件:大於四個字
                if len(input_word) >= 4:
                    keyword = input_word

                    # word = None
                    for i in range(len(keyword)):
                        word = keyword[i]

                        if i == len(keyword) - 1:
                            next_word = None
                        else:
                            next_word = keyword[i+1]

                        #找到專屬dict
                        if i ==0:
                            diction = self.dict_map[self.letter_dict[word]][word]
                        else:
                            if word not in diction:
                                diction[word] = {}
                            if i == len(keyword) - 1:
                                diction[word][next_word] = next_word

                            diction = diction[word]


    def lookup_dict_diciton(self,txt):
        for i in range(len(txt)):
            word = txt[i]
            if i == 0:
                d = self.dict_map[self.letter_dict[word]][word]
                # print(d)
            else:
                if word in d:
                    d = d[word]
                    # print(f"{txt} , {word} ok")

                    if i == len(txt)-1:

                        # print(d[word])
                        if None in d:
                            # print(f"{txt} , is word ")
                            return 2
                        else:
                            # print(f"{txt} , is not word")
                            return 1

                        # print(f"{txt} , is not in diction")
        if len(txt) == 1:
            return  1
        else:
            return 9


def main():
    dd = Dictionary_Dict()
    dd.diction_dict()

    ds = Dictionary_Set()
    ds.diction_s()


    txt = ['arm','art','act','book','beck','bool']
    for keyword in txt:
        dd.lookup_dict_diciton(keyword)
        ds.lookup_set_diction(keyword)

if __name__ == '__main__':
    main()
