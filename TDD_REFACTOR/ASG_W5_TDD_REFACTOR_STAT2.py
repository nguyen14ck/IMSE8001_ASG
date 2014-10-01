
from TDDUtils import *
import math

print("TDD + REFACTOR\n")
f=open('dataset1.csv')
w=open('dataset1-convert.csv','w')

#########################################



header=f.readline()[:-1]
#print(header)
assert "x1,x2" == header
w.write("x1,x2,x1px2,x1mx2\n")

for l in f:
    l=l[:-1]
    #print(l)
    x1,x2=l.split(',')
    x1,x2=float(x1),float(x2)
    #print(x1,x2)
    r=[x1,x2,x1+x2,x2-x1]
    r=map(lambda x: str(x),r)
    w.write(','.join(r)+"\n")

w.close()


#########################################

def nAr(n,r):
        ft = math.factorial
        return ft(n) / ft(n-r)


#CLASS DATA READER   
class Data_Reader:
    def __init__(self,file_name):
        self.file_name = file_name
        self.fl = open(self.file_name)
        self.header=self.fl.readline()[:-1]
        #print(header)
        

    def readFile(self):
        #self.fl = open(self.file_name)
        print(self.fl)
        print('\n')
        return True
    
    def readHeader(self):
        header=self.fl.readline()
        header=self.fl.readline()
        print(header)
        return True
    

    def countLines(self):
        self.num_lines = sum(1 for line in self.fl)
        print('Lines: ' + str(self.num_lines + 1) +'\n')
        return self.num_lines + 1

    def countNodes(self,num_lines):
        return num_lines - 1 #assume line 1 is header

    def countArcs(self, num_nodes):
        ft = math.factorial
        return ft(num_nodes) / ft(num_nodes-2)
    
        
    def countCols(self):
        hd = self.header.split(',')
        ncols = len(hd)
        print('Number of columns: ' + str(ncols))
        print(hd)
        return ncols
  
    
dtr = Data_Reader('dataset1.csv')
dtr.readFile()

nLines = dtr.countLines()
#print(type(nLines))
assertEquals(int(30),nLines,'Test output of the Data_Reader instance: number of Lines')


nNodes = dtr.countNodes(nLines)

#print(type(nNodes))
print('Nodes: ' + str(nNodes) + '\n')
assertEquals(int(29),nNodes,'Test output of the Data_Reader instance: number of Nodes')

nArcs = dtr.countArcs(nNodes)
#print(type(nArcs))
print('Arcs: ' + str(nArcs) + '\n')
assertEquals(long(812),nArcs,'Test output of the Data_Reader instance: number of Arcs')



dtr.countCols()
#print(type(dtr.countCols()))
assertEquals(int(2),dtr.countCols(),'Test output of the Data_Reader instance: number of Columns')







