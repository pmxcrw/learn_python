
class Unsplice():
    
    def __init__(self, input, splice = "\\\n"):
        self.splice = splice
        self.input = input
    
    def unsplice(self):
        return self.input.replace(self.splice, "")
