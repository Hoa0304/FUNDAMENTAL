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
from abc import ABC, abstractmethod

class person:
    def __init__(self, name, age, appearance):
        self.name = name
        self.age = age
        self.__appearance = appearance
        
    def getAppearance(self):
        return self.__appearance
    def setAppearance(self, value):
        self.__appearance = value
    
    @abstractmethod
    def learnEnglish(self):
        pass

class CamHoa(person):
    
    def learnEnglish(self):
        print(f"{self.name} is learning English.")
    
    def newSentence(self):
        print("No pain, no gain")
        
class DucDat(person):
    def __init__(self, name, age, appearance, location):
        super().__init__(name, age, appearance)
        self.location = location
        
    def learnEnglish(self):
        pass
    
    def newSentence(self):
        print("sleep")
        
ch = CamHoa("Tran Thi Cam Hoa", 22, "cute")
print(ch.name)
ch.newSentence()

dd = DucDat("Nguyen Duc Dat", 22, "xau", "Quang Binh" )
print(dd.location)

#------------Polymorphism--------
# hỗ trợ inheritance, khác là chỉ những object ở nhiều dạng
# ví dụ: CamHoa với newSentence là No pain, no gain nhưng ở DucDat thì sleep

#------------Encapsulation--------
# Tính đóng gói: private, public, protected và default
print(ch.getAppearance())

#------------Abstraction--------
# trừu tượng: chỉ show ra những thông tin cần thiết cho user, uer k qtam cách hoạt động của method như nào
ch.learnEnglish()  
