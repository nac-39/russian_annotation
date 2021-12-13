import pymorphy2
import re

class Dictionaries():
    def __init__(self) -> None:
        self.case = {
            "nomn":"主",
            "gent":"生",
            "datv":"与",
            "accs":"対",
            "ablt":"造",
            "loct":"前",
            "voct":"呼",
            "gen2":"属2",
            "acc2":"対2",
            "loc2":"前2",
        }

        self.number = {
            "sing":"単",
            "plur":"複",
        }

        self.gender = {
            "masc":"男",
            "femn":"女",
            "neut":"中",
        }

        self.other = {
            "LATN":"",#ラテン文字
            "PNCT":"",#句読点
            "NUMB":"",#数字
            "intg":"",#整数
            "real":"",#実数
            "ROMN":"",#ローマ数字
            "UNKN":"",#不明
        }

        self.hinsshi = {
            'NOUN':"名",
            'ADJF':"形",
            'ADJS':"形短",
            'VERB':"動",
            'INFN':"動",        
            'PRTF':"形動",#"形動詞・形容分詞",        
            'PRTS':"形動(短)",#"形動詞・形容分詞（短）",
            'GRND':"動名",
            'COMP':"比",
            'PREP':"前",        
            'CONJ':"接",
            'INTJ':"間",
            'PRCL':"助",
            'ADVB':"副",
            'NPRO':"代",
            'PRED':"述",
            'NUMR':"数"
        }

        self.ignore_pos = {
            "PNCT",
            "PEWP",
            "UNKN",
            "None",
        }

class RUSwords:
    def __init__(self,word):
            self.word = word
            self.morph = pymorphy2.analyzer.MorphAnalyzer()
            self.d = Dictionaries()
    
    #形態素解析する関数
    def parse(self,word):
        p = self.morph.parse(word)[0]
        return p
    
    #出力用関数
    def output(self):
        d = self.d
        tags = set(str(self.tags()).split(","))
        if tags.isdisjoint(d.ignore_pos):
            try:
                case = d.case[self.case()]
            except:
                case = ""
            try:
                hinshi = d.hinsshi[self.pos()]
            except:
                hinshi = ""
            try:
                gender = d.gender[self.gender()]
            except:
                gender = ""
            try:
                nomal = self.nomal()
                if self.word.lower == nomal:
                    nomal = ""
            except:
                nomal = ""
            txt = f"{case}{hinshi}{gender}{nomal}"
            return (case,hinshi,gender,nomal)
        else:
            tags = "".join(list(tags))
            try:
                return ("",d.hinsshi[tags],"",)
            except:
                try:
                    return (d.other[tags],"","","")
                except:
                    return ("","","","")

    #タグを抽出
    def tags(self):
        return self.parse(self.word).tag

    #品詞
    def pos(self):
        return self.tags().POS

    #格
    def case(self):
        a  =self.tags()
        return a.case
    
    #名詞の性
    def gender(self):
        return self.tags().gender

    #基本形
    def nomal(self):
        return self.morph.normal_forms(self.word)[0]

def gen_ruword(ru):
    ru = re.sub(r'(\W)', r' \1 ',ru)
    ru = re.sub(r"(\s)+"," ",ru)
    ru_list = re.split(" ",ru)
    ru_list = [w.replace(" ","") for w in ru_list]
    for i in range(len(ru_list)):
        word = ru_list[i]
        r = RUSwords(word)
        ru_list[i] = [ru_list[i],r.output()]
    return ru_list

def lower_calse(word):
    new_w = pymorphy2.shapes.restore_capitalization(word,"дододо")
    return new_w


if __name__=="__main__":
    f = open("ru_txt.txt","r")
    ru = f.read().replace("."," . ").replace(","," , ").replace(":"," : ").split(" ")
    f.close()

    for word in ru:
        r = RUSwords(word)
        print(f"{word}:{r.output()}")
