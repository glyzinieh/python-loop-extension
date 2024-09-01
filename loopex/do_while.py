class DoWhile:
    def __init__(self):
        self.first = True

    def do_while(self, condition):
        if self.first:
            self.first = False
            return True
        else:
            return condition
