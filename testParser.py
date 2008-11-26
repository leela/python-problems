import csvParser

class myFile:
    def __init__(self, data):
        self.csv = data
    def readlines(self):
        return self.csv.split('\n')

def test():
    text = "a,b,c\n1,2,3,4"
    fObj = myFile(text)
    print csvParser.parse_csv(fObj)

if __name__ == "__main__":
    test()
