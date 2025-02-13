class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

object_ref = Calc(3, 4)
output = object_ref.sum()
print(output)
