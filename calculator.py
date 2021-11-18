class Calc:
    def multiply(self, x, y):
        return x * y
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def div(self, x, y):
        if y == 0:
            print("на ноль делить нельзя")
        else:
            return x / y