abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
print(abc[1:])
print(abc[:-1])
print(abc[2:5:2])
print(abc[-5:-2])
print(abc[::-1])
print(abc[::-2])



class Inherit:

    def __init__(self):
        self.head = "head"
        self.tails()

    def tails(self):
        print("This is the tail")

class GetInheritance(Inherit):

    def __init__(self):
        super().__init__()
        self.body = "body"

get = GetInheritance()
print(get.body)

