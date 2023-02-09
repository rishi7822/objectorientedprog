#declare class

class Anime:
    #def function
    def __init__(self,name,genre,year):
        self.name = name
        self.genre = genre
        self.year = year

tokyo = Anime("naruto","adventure",2007)
kyuto = Anime("tokyo rvengers","Action",2022)

#print

print(tokyo.name)
print(kyuto.genre)