class CamHoa:
    def __init__(self, name, age, appearance):
        self.name = name
        self.age = age
        self.appearance = appearance
    
    def learnEnglish(self):
        pass
    
    def newSentence(self):
        print("No pain, no gain")
    
ch = CamHoa("Tran Thi Cam Hoa", 22, "mapp")
print(ch.name)
ch.newSentence()

## set private self.__appearance = appearance