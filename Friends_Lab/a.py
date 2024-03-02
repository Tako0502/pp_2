class Labaratory:
    def __init__(self,name,boss,numOfemplayers,numOfprojects):
        self.name = name
        self.boss = boss
        self.numOfemplayers = numOfemplayers
        self.numOfprojects = numOfprojects
    def info(self):
        print(f"название : {self.name}  ,заведующий : {self.boss} , количество сотрудников : {self.numOfemplayers} , количество проектов :  {self.numOfprojects}")
labaratory = Labaratory(name = "<NAME>",boss = "<NAME>",numOfemplayers = 10,numOfprojects = 10)
labaratory.info()