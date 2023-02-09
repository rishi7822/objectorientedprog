class Players:
    #use the def __init__ funtion
    def __init__(self, fname,lname,salary):
        #self function


        self.fname = fname
        self.lname = lname
        self.salary = salary



ronaldo = Players("ronaldo", "cristiano",  39999999)
messi = Players("messi", "lionel",  8893994934)

print(messi.salary, ronaldo.salary)