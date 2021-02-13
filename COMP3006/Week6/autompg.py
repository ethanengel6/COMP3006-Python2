
def main():

    import csv
    from collections import namedtuple

    ad = AutoMPGData()
    for a in ad:
        busted=a.I.split()
        make=busted[0]
        busted=busted[1:]
        separator = ' '
        model=separator.join(busted)
        hooptie=AutoMPG(make," "+model," "+a.G," "+a.F)
        print(str(hooptie))

class AutoMPG:

    def __init__(self,make,model,year,mpg):
        self.make=make
        self.model=model
        self.year=year
        self.mpg=mpg

    def __repr__ (self):
        return '{make:'+self.make+', model:'+self.model+', year:'+str(self.year)+', mpg:'+str(self.mpg)+'}'

    def __str__(self):
        return f"AutoMPG({self.make},{self.model},{self.year},{self.mpg})"

    def __eq__(self,other):
        if type(self)==type(other):
            return self.make==other.make and self.model==other.model and self.year==other.year and self.mpg==other.mpg
        else:
            return NotImplemented

    def __lt__(self,other):
        if type(self)==type(other):
            return (self.make,self.model,self.year,self.mpg) < (other.make,other.model,other.year,other.mpg)
        else:
            return

    def __hash__ (self):
        return hash((self.make,self.model,self.year,self.mpg))

class AutoMPGData:
    data=[]

    def __init__(self):
        data=self.data
        self._clean_data()
        self._load_data()

    def __iter__(self):
        return (x for x in self.data)

    def _load_data(self):
        with open('auto-mpg.clean.txt','r') as f2:
            self.data = self._process_data(f2)
            return self.data

    def _process_data(self, input):
        import csv
        from collections import namedtuple
        cleanread=csv.reader(input,delimiter=" ",skipinitialspace=True)
        Record = namedtuple('Record', 'A B C D E F G H I')
        data = []
        for row in cleanread:
            nt = Record(row[0],row[1],row[2],row[3],row[4],row[5],'19'+row[6],row[7],row[8])
            data.append(nt)
        return data

    def process_lines(file,input):
        import csv
        from collections import namedtuple
        cleanread2=csv.reader(input,delimiter=" ",skipinitialspace=True)
        Record2 = namedtuple('Record2', 'A B C D E F G H I')
        data2 = []
        for row in cleanread[:2]:
            nt2 = Record(row[0],row[1],row[2],row[3],row[4],row[5],'19'+row[6],row[7],row[8])
            data2.append(nt2)
        return data2

    def _clean_data(self):
        import csv
        with open('auto-mpg.data.txt', 'r') as f:
            read = csv.reader(f)
            rowslist=[]
            for row in read:
                rowslist.append(row[0].expandtabs()+'\n')

        with open('auto-mpg.clean.txt','w') as write:
            for lines in rowslist:
                write.writelines(rowslist)






if __name__ == '__main__':

        main()
