# class CamHoa:
#     def __init__(self, name, age, appearance):
#         self.name = name
#         self.age = age
#         self.appearance = appearance
    
#     def learnEnglish(self):
#         pass
    
#     def newSentence(self):
#         print("No pain, no gain")
    
# ch = CamHoa("Tran Thi Cam Hoa", 22, "mapp")
# print(ch.name)
# ch.newSentence()

## set private self.__appearance = appearance

#------------Inheritance--------

class person:
    def __init__(self, name, age, appearance):
        self.name = name
        self.age = age
        self.appearance = appearance

class CamHoa(person):
    
    def learnEnglish(self):
        pass
    
    def newSentence(self):
        print("No pain, no gain")
        
class DucDat(person):
    def __init__(self, name, age, appearance, location):
        super().__init__(name, age, appearance)
        self.location = location
        
    def learnEnglish(self):
        pass
    
    def newSentence(self):
        print("No pain, no gain")
        
ch = CamHoa("Tran Thi Cam Hoa", 22, "cute")
print(ch.name)
ch.newSentence()

dd = DucDat("Nguyen Duc Dat", 22, "xau", "Quang Binh" )
print(dd.location)
